from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid(): #우리가 입력된 데이터가 규격에 맞다면 True를 반환. 검증 기능
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            # article = Article.objects.create(title=title, content=content) #.create는 .save 없이 생성 가능하게 한다.
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
        #여기선 괄호 붙여서 인스턴스로 만들자. 위에 만든 변수를 html에 객체로 갖다쓰자.
    
    return render(request, 'form.html', {'form':form})
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid(): 
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
        
    
    return render(request, 'form.html', {'form':form})
    