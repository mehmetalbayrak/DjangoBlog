from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpRequest

# Create your views here.

def index(request):
    allBlogs = models.Blog.objects.all().order_by('-createdDate')
    chunked_items = list(chunked_list(allBlogs, 2))
    return render(request,'blog_app/index.html',{'chunked_items' :chunked_items})

def blogdetail(request,url):
    blog = models.Blog.objects.get(urlSlug = url)
    blog.keywords = blog.keywords.split(',')
    blog.canonical_url = request.build_absolute_uri()

    blog_dict = {"blog" : blog}
    return render(request,'blog_app/blog-detail.html',blog_dict)



def chunked_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
