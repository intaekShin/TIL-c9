from django import forms
from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')
    # max_length가 필수가 아님.
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '내용을 입력하세요.',
    }))
    
class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(label='제목') #models.py에 있는 값을 덮어쓴다.
    
    class Meta: #위 클래스의 정보를 담는 그릇 역할
        model = Article
        fields = ['title', 'content']
    