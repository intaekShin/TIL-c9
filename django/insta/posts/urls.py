from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'), 
    # <>부분은 variable routing 이라고 각기 다른 값을 넣을 수 있다.
    path('<int:post_id>/comments/create/', views.comment_create, name ='comment_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete', views.comment_delete, name = 'comment_delete'),
    path('<int:post_id>/like/', views.like, name = 'like'),
    
]