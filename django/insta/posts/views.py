from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


def list(request):
    posts = Post.objects.order_by('-id').all()      # 내림차순 정렬을 해서 가져옴.order_by('-id') 
    return render(request, 'posts/list.html', {'posts': posts})


# from django.contrib.auth.decorators import login_required     @ : 데코레이터, 파이썬에서 쓰이는 문법, 함수 바로 위쪽에 메소드로써 적용. 아래부분을 데코레이터의 파라미터로 적용.
@login_required         # login 이 충족이 되었는지 검사하고 충족하지 않았으면 login 함수 실행. 그리고 주소에 /?next=/posts/create가 남음.
def create(request):
    if request.method == 'POST':
        # request.POST #=> {'content':'asdf', 'user':'1'}
        post_form = PostForm(request.POST, request.FILES)   # 원래 data=request.POST, files=request.FILES 를 줄인 거임.
        if post_form.is_valid():        # 데이터베이스에 넣어도 문제 없느냐? 묻는 코드.
            post= post_form.save(commit=False)
            post.user = request.user
            post.save()                 # 실제 데이터 베이스에 저장.
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/form.html', {'post_form' : post_form}) # 틀을 잡고 살을 붙여나가는 방식으로 진행할 예정.


def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:       # id가 다른 경우 거르는 if문을 제일 위에 작성하는 것.
        return redirect('posts:list')
        
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'post_form' : post_form})
    
    
def delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:       # id가 다른 경우 거르는 if문을 제일 위에 작성하는 것.
        return redirect('posts:list')
        
    post.delete()
    
    # if post.user != request.user:   
    #     post.delete()
    
    return redirect('posts:list')