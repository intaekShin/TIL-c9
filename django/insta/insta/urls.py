"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static      # static method 가져오기.
from django.conf import settings                # settings.py 의 file을 가져오기.
from accounts import views as accounts_views    # 이름 혼동을 피하기 위해 accounts_views  변수명을 변경.



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),    # 대괄호 안에 내용물 뒤에 ,쉼표를 꼭 붙이는 습관을 들이는 게 좋다.
    path('posts/', include('posts.urls')),
    path('<str:username>/', accounts_views.people, name = 'people'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 주소를 업로드.
