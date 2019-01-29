from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:student_id>/', views.detail),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/update/', views.update),
    ]

# path('', views.index),
#     path('new/', views.new),
#     path('create/', views.create),
#     path('<int:post_id>/', views.detail),
#     path('<int:post_id>/delete/', views.delete),
#     path('<int:post_id>/edit/', views.edit),
#     path('<int:post_id>/update/', views.update),