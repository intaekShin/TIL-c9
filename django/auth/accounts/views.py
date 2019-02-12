from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #django에서 미리 만들어놓은 폼 하나를 import하자.
from django.contrib.auth import login as auth_login #함수 이름을 변경한 것이고 실제로 똑같이 동작한다.
from django.contrib.auth import logout as auth_logout

# Create your views here.

# django에서 이미 User에 대한 틀을 미리 다 만들어 놨다. create 함수 만들 때처럼 나들면 된다.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #form 객체 생성.
        if form.is_valid(): #규격에 맞는지 확인 
            user = form.save() #유저 생성.
            auth_login(request, user)
            return redirect('posts:list') #주소  list로 다시 가기.
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form':form}) #변수를 html로 가져갈 변수로 쓰기.

# Session Create    
def login(request):
    #로그인은 마찬가지로 하나 create하는 건데... session이라는 것을 create하는 것이다.
    #간단하게 말하자면 정보 임시 저장 공간을 뜻한다. 페이지 전환을 하더라도 정보가 유지 된다.
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) #get_user가 user의 데이터를 가져온다. auth_login이 session에 저장해준다.
            return redirect(request.GET.get('next') or 'posts:list') # request.GET.get('next') $=> /posts/new/
            # request.GET은 GET형식을 의히하고 GET형식은 주소값을 보내는 것. GET값은 딕셔너리 형태로 있으므로 .get은 key값을 호출(next)하며 해당하는 value값. 즉, 이 코드에선 /posts/new/를 호출한다.
    else:
        form = AuthenticationForm() #진짜로 존재하는지 검증하는 form 
    
    
    return render(request, 'login.html', {'form':form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')