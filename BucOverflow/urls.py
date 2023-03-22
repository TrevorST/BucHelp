from django.urls import path, include

from . import views
from .views import base, index, discussions, home, SignUpView

app_name = "BucOverflow"

urlpatterns = [
    path("", views.base, name="base"),
    path("index", views.index, name="index"),
    path("discussions", views.discussions, name="discussions"),
    path("home", views.home, name="home"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("post/<slug>/", views.post, name="post"),
    #path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("createpost", views.create_post, name="createpost"),
    path("profile/<slug>/", views.profile, name="profile"),
     #url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
]
