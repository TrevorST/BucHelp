from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

# Forms python fuctionality for user data (Username & Password)
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

# Forms Post dara for model Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {"title","content"}