from django.shortcuts import render, redirect
from .models import Post
# 현재 폴더안에 있는 models파일을 그리고 그 중에  Post class를 임포트 한다.
# Create your views here.
# views.py -> urls.py -> templates

def new(request):
    return render(request, 'new.html')

def create(request):
    # request.GET / request.POST
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return redirect('posts:detail', post.pk)
    
def index(request):
    # All Post
    posts = Post.objects.all() # => [< >, < >, < >]
    
    return render(request, 'index.html', {'posts' : posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post' : post} )
    
# def naver(request, q):
#     return redirect(f'https://search.naver.com/search.naver?query={q}')
    
# def github(request, username):
#     return redirect(f'https://github.com/{username}')
#     # path('github/intaekShin')

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})
    
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('posts:detail', post.pk)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    