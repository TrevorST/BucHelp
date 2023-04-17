from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
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
from django.apps import AppConfig
from django.core.signals import setting_changed


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
    
    #post = Post.objects.filter(slug = slug)
    profile = get_object_or_404(Author, slug=slug) #404 object not found
    karma= 0
    #update users karma
    posts = Post.objects.filter(user=profile)
    for post in posts:
        karma+=post.karma
    profile.karma = karma

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
    postsliked = []
    postsdisliked = []
    if request.user.is_authenticated:  # Notice this condition
        #now get the author or current user
        author = Author.objects.get(user=request.user)
        for post in posts:
            #update karma for posts
            post.update_karma()
            post.save()
            #if user has liked this post
            if post.likes.filter(user=author.user).exists(): #might need to overwrite author equals val
                postsliked.append(post.id) 
            if post.dislikes.filter(user=author.user).exists(): #might need to overwrite author equals val
                postsdisliked.append(post.id) 
            comments = post.comments.all()
            for comment in comments:
                comment.getTimeElapsed()
                comment.save()
    else: #user is not autheticated aka signed in
        for post in posts:
             #update karma for posts
            post.update_karma()
            post.save()
            comments = post.comments.all()
            for comment in comments:
                comment.getTimeElapsed()
                comment.save()

    test=search(posts, "laundry")
    print(test)
    context = { 'posts' : posts,
                'postsliked' : postsliked,
                'postsdisliked' : postsdisliked}
    return render(request, "discussions.html", context)

@login_required(login_url='/signin/')
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


#user likes post
@login_required(login_url='/signin/')
def like_post(request):
    #use id from ajax post
    post = get_object_or_404(Post, id=request.POST.get('id')) #404 object not found 

    #now get the author that liked the post
    author = Author.objects.get(user=request.user)

    is_liked = False
    if post.likes.filter(id=author.id).exists():
        post.likes.remove(author)
        is_liked = False
    else:
        post.likes.add(author)
        is_liked = True
        #check if they had it disliked
        if post.dislikes.filter(id=author.id).exists():
            post.dislikes.remove(author)
    post.update_karma()
    post.save()
    #context = { 'posts' : posts,}
    return render(request, "discussions.html")

    #user dislikes post
@login_required(login_url='/signin/')
def dislike_post(request):
    #use id from ajax post
    post = get_object_or_404(Post, id=request.POST.get('id')) #404 object not found 

    #now get the author that liked the post
    author = Author.objects.get(user=request.user)

    is_disliked = False
    if post.dislikes.filter(id=author.id).exists():
        post.dislikes.remove(author)
        is_disliked = False
    else:
        post.dislikes.add(author)
        is_disliked = True
        #check if they had it liked
        if post.likes.filter(id=author.id).exists():
            post.likes.remove(author)
    post.update_karma()
    post.save()
    return render(request, "discussions.html")

#return sorted list
def search(posts, search):
    count = 0
    highestCount = 0
    mostRelevantPost= posts[0]
    temp=""
    for post in posts:
        count = 0
        #for each post object get the number of matches
        for element in post.title:
            #do not exceede search string length
            if(count<len(search)):
                if(search[count] == element):
                    count += 1
        if count > highestCount:
            highestCount = count
            mostRelevantPost = post
            
    return mostRelevantPost

        