from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/delete/', views.delete, name='delete'), # <>부분은 variable routing 이라고 각기 다른 값을 넣을 수 있다.
]