from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def index(request):
    pass
