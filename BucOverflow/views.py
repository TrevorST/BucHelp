from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    return HttpResponse("WELCOME TO BUCOVERFLOW")
# Create your views here.

def dashboard(request):
    return render(request, "dwitter/dashboard.html")
