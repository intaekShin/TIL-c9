from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm, ImageFormSet
from .models import Post, Comment
from django.db import transaction


def list(request):
    posts = Post.objects.order_by('-id').all()      
    # 내림차순 정렬을 해서 가져옴.order_by('-id') 
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form': comment_form})


# from django.contrib.auth.decorators import login_required     @ : 데코레이터, 파이썬에서 쓰이는 문법, 함수 바로 위쪽에 메소드로써 적용. 아래부분을 데코레이터의 파라미터로 적용.
@login_required         # login 이 충족이 되었는지 검사하고 충족하지 않았으면 login 함수 실행. 그리고 주소에 /?next=/posts/create가 남음.
def create(request):
    if request.method == 'POST':
        # request.POST #=> {'content':'asdf', 'user':'1'}
        post_form = PostForm(request.POST)   # 원래 data=request.POST, files=request.FILES 를 줄인 거임.
        image_formset = ImageFormSet(request.POST, request.FILES)
        if post_form.is_valid() and image_formset.is_valid():        # 데이터베이스에 넣어도 문제 없느냐? 묻는 코드.
            post= post_form.save(commit=False)
            post.user = request.user
            
            # from django.db import transaction
            with transaction.atomic():
                # 첫번째 포스트가 먼저 생성이 되야하고
                post.save()          # 실제 데이터 베이스에 저장. 그래야 id값이 나오니깐요.
                # 두번째 생성된 포스트를 바탕으로
                image_formset.instance = post   # 난 얘꺼다. 표시하기~~!
                image_formset.save() # 실제 데이터베이스에 저장
                # 사고를 방지하는 메소드가 있다. 순서에 관한 사고.
            
            
            return redirect('posts:list')
    else:
        post_form = PostForm()
        # 이미지 폼셋도 넘겨주자
        image_formset = ImageFormSet()
    return render(request, 'posts/form.html', {
                                            'post_form' : post_form, 
                                            'image_formset':image_formset,
        
    }) # 틀을 잡고 살을 붙여나가는 방식으로 진행할 예정. 딕셔너리는 몇줄로 이루어져도 괜찮음.


@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:       # id가 다른 경우 거르는 if문을 제일 위에 작성하는 것.
        return redirect('posts:list')
        
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
        image_formset = ImageFormSet(instance=post)
    return render(request, 'posts/form.html', {'post_form' : post_form, 'image_formset':image_formset,})
    

@login_required    
def delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:       # id가 다른 경우 거르는 if문을 제일 위에 작성하는 것.
        return redirect('posts:list')
        
    post.delete()
    
    # if post.user != request.user:   
    #     post.delete()
    
    return redirect('posts:list')
    

# from django.views.decorators.http import require_POST
@login_required # 데코레이터도 순서에 영향을 받는다.
@require_POST   # POST로 오는 요청만 받겠다. 주소를 직접 입력하는 것은 GET요청방식이다.
def comment_create(request, post_id): 
    # post_id를 통해 post에 대한 정보를 받아와서 조작한다.
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # DB에 반영없이 객체만 만든다.
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list')
    

@require_http_methods(['GET', 'POST']) # require_POST,GET 과 같은 기능. 다양한 방식이 허용된다.
def comment_delete(request, post_id, comment_id):
    # from .models import Comment
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user != request.user:    # 다른사람이면 지우면 안된다.
        return redirect('posts:list')
        
    comment.delete()
    return redirect('posts:list')
    

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():
        # 2. 좋아요 취소
        post.like_users.remove(request.user)
    else:
        # 1. 좋아요 !
        post.like_users.add(request.user) # requst.user 로그인된 유저.
    return redirect('posts:list')
    