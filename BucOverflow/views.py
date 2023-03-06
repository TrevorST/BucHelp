from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse
from . import models
from .models import Post

##REGISTRATION///LOGIN imports//
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#####REGISTRATION///LOGIN####
def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context.update({
        "form": form,
        "title": "Signin",
    })
    return render(request, "signin.html", context)







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


    

