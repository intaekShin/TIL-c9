from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile

# Create your views here.
# 회원가입 기능
def signup(request):
    if request.user.is_authenticated:       # 로그인이 되어있으면 
        return redirect('posts:list')       # 튕겨낸다.
    
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) # User Profile 생성
            auth_login(request, user)  # 회원가입하자마자 로그인이 자동으로 되게끔 하는 코드.
            return redirect('posts:list')
    else:
        signup_form = CustomUserCreationForm()
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
    
    
# User Edit(회원정보 수정) - User CRUD 중 U
# from .forms import CustomUserChangeForm
# from django.contrib.auth.decorators import login_required
@login_required
def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = password_change_form.save()  # 로그인 된 상태 유지.
            update_session_autH_hash(request, user)
            return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {
                                        'user_change_form' : user_change_form
    })
    

# User Delete(회원 탈퇴) - User CRUD 중 D
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')
    
    
# from django.contrib.auth.forms import PasswordChangeForm    
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user) 
            # 유저정보가 변경되면 session이 만료되어서 자동으로 로그인이 해제된다. 
            # 위 코드가 변경된 회원정보를 session에 다시 입력하기 때문에 로그인이 풀리지 않는다.
            return redirect('people', request.user.username)
        
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html', {
                                        'password_change_form':password_change_form, 
    })
    
    
# from .forms import CustomUserChangeForm, ProfileForm    
def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance = profile)
    return render(request, 'accounts/profile_update.html', {'profile_form': profile_form,})
    

def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id=user_id)
    
    if request.user in people.followers.all():
        # 2. people을 unfollow하기
        people.followers.remove(request.user)
    else:
        # 1. people을 follow하기
        people.followers.add(request.user)
    
    return redirect('people', people.username)