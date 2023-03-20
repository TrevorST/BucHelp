from django.urls import path, include

from . import views
from .views import base, index, discussions, home

app_name = "BucOverflow"

urlpatterns = [
    path("", views.base, name="base"),
    path("index", views.index, name="index"),
    path("discussions", views.discussions, name="discussions"),
    path("home", views.home, name="home"),
    path("post/<slug>/", views.post, name="post"),
    #path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
     #url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
]
