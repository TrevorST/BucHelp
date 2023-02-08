from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("WELCOME TO BUCOVERFLOW")
# Create your views here.
