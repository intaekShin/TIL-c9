from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model


# Create your views here.
# 회원가입 기능
def signup(request):
    if request.user.is_authenticated:       # 로그인이 되어있으면 
        return redirect('posts:list')       # 튕겨낸다.
    
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)  # 회원가입하자마자 로그인이 자동으로 되게끔 하는 코드.
            return redirect('posts:list')
    else:
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})
    
# from django.contrib.auth import login as auth_login
def login(request):
    if request.user.is_authenticated:       # 로그인이 되어있으면 
        return redirect('posts:list')       # 튕겨낸다.
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')    # login 을 실행후에 주소에 next값이 있으면 next뒤 주소로 리다이렉트.
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    

# from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
# from django.shortcuts import get_object_or_404    
# from django.contrib.auth import get_user_model
def people(request, username):
    # get_user_model() #=> User
    people = get_object_or_404(get_user_model(), username=username) 
    # 앞username 은 컬럼의 username // 뒤username은 매개변수 username
    return render(request, 'accounts/people.html', {'people':people})