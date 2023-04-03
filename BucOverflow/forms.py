from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {"title","content"}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"content"}