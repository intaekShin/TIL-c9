from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():        # 데이터베이스에 넣어도 문제 없느냐? 묻는 코드.
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form' : post_form}) # 틀을 잡고 살을 붙여나가는 방식으로 진행할 예정.
    
    
def delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:list')