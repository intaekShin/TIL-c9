from django.shortcuts import render
from .models import Post
# 현재 폴더안에 있는 models파일을 그리고 그 중에  Post class를 임포트 한다.
# Create your views here.
# views.py -> urls.py -> templates

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return render(request, 'create.html')
    
def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts' : posts})