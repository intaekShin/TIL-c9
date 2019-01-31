from django.shortcuts import render, redirect
from .models import Post, Comment
# 현재 폴더안에 있는 models파일을 그리고 그 중에  Post class를 임포트 한다.
# Create your views here.
# views.py -> urls.py -> templates

def new(request):
    return render(request, 'new.html')

def create(request):
    # request.GET / request.POST
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')
    
    # DB INSERT
    post = Post(title=title, content=content, image=image)
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
    
def comments_create(request, post_id):
    # 댓글을 달 게시물
    post = Post.objects.get(pk=post_id)
    
    # form에서 넘어온 댓글 내용
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content) #인스턴스 생성.
    comment.save()
    
    return redirect('posts:detail', post.pk)
    
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)
    
    