from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    # path('', views.list, name = 'list'),
    path('', views.PersonList.as_view(), name = 'list'),
    # path('create/', views.create, name = 'create'),
    path('create/', views.PersonCreate.as_view(), name = 'create'),
    
]
