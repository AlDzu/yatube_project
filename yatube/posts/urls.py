# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [

    #Главная страница
    path('', views.index),
    #Список постов после групп
    path('group/<slug:slug>/', views.group_posts),
] 