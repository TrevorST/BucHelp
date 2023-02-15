from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from .models import Post

# Create your views here.

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def discussions(request):
    return render(request, "discussions.html")

