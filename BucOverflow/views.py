from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from .models import Post

def index(request):
    return HttpResponse("WELCOME TO BUCOVERFLOW")
# Create your views here.

def dashboard(request):
    posts = Post.objects.all()
    context = {'posts' : posts,}
    return render(request, "dashboard.html", context)
