from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {"title","content"}