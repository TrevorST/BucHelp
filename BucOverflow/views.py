from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse
from . import models
from .models import Post

# Create your views here.
# url "" should be the index and show the forum d
# url "post/" + post.title should show the post details

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")


def post(request, slug):
    #post = get_list_or_404
     #post = Post.objects.filter(slug = slug)
     post = get_object_or_404(Post, slug=slug) #404 object not found

     context = { 'post' : post,}

     return render(request, "post.html", context)

def discussions(request):
    posts = Post.objects.all()
    context = { 'posts' : posts,}
    return render(request, "discussions.html", context)


    

