from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def homeredirect():
    return HttpResponse.request

def discussions(request):
    return render(request, "discussions.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('BucOverflow:home')

