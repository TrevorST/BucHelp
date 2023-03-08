from django.urls import path, include
from django.conf.urls import url

from . import views
from .views import base, index, discussions, home, SignUpView

app_name = "BucOverflow"

urlpatterns = [
    path("", views.base, name="base"),
    path("index", views.index, name="index"),
    path("discussions", views.discussions, name="discussions"),
    path("home", views.home, name="home"),
<<<<<<< HEAD
    path("signup", SignUpView.as_view(), name="signup"),
    path("post/<slug>/", views.post, name="post"),
    #path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
     #url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
=======
    path("login", views.login, name="login"),
>>>>>>> 8a040746b02d4366bc5c9d31387a5f040e15e1e9
]
