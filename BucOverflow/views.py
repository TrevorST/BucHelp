from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Author
from django.contrib.auth.models import User
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse
from . import models
from .forms import SignUpForm, PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

##REGISTRATION///LOGIN imports//
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout as lt


# Create your views here.
# url "" should be the index and show the forum d
# url "post/" + post.title should show the post details

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def ourteam(request):
    return render(request, "ourteam.html")

def report(request):
    return render(request, "report.html")

def homeredirect():
    return HttpResponse.request


def profile(request, slug):
    #post = get_list_or_404
     #post = Post.objects.filter(slug = slug)
     profile = get_object_or_404(Author, slug=slug) #404 object not found

     context = { 'profile' : profile,}

     return render(request, "profile.html", context)

def post(request, slug):
    #post = get_list_or_404
     #post = Post.objects.filter(slug = slug)
     post = get_object_or_404(Post, slug=slug) #404 object not found

     form = CommentForm(request.POST or None)
     if request.method == "POST":
        if form.is_valid():
            #get the post
            post = Post.objects.get(slug=slug)
            print("\n\n valid post!")
            author = Author.objects.get(user=request.user)
            new_comment = form.save(commit=False)
            new_comment.user = author
            new_comment.save()
            post.comments.add(new_comment)
            form.save_m2m()

     context = { 'post' : post,}

     return render(request, "post.html", context)

def discussions(request):
    posts = Post.objects.all()
    context = { 'posts' : posts,}
    return render(request, "discussions.html", context)

@login_required
def create_post(request):
    context = {}
    #use to check if our POST is valid
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
             print("\n\n valid post!")
             author = Author.objects.get(user=request.user)
             new_post = form.save(commit=False)
             new_post.user = author
             new_post.save()
             form.save_m2m()
             return redirect("/home")
    context.update({
        "form": form,
        "title": "Create New Post"
    })
    return render(request, "create_post.html", context)



#####REGISTRATION///LOGIN####
def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        #username = request.POST['username']
        #password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #sucsess
            login(request, user)
            return redirect("/home")
    context.update({
        "form": form,
        "title": "Signin",
    })
    return render(request, "signin.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("/home")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('BucOverflow:home')

