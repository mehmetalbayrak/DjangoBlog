from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blog_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:url>/', views.blogdetail, name="blogdetail"),
]