from django.urls import path, include

from . import views
from .views import base, discussions, home, about, ourteam, report, SignUpView

app_name = "BucOverflow"

# URL patterns for path navigational information

urlpatterns = [
    path("", views.home, name="base"),
    path("discussions", views.discussions, name="discussions"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("ourteam", views.ourteam, name="ourteam"),
    path("report", views.report, name="report"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("post/<slug>/", views.post, name="post"),
    #path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("createpost", views.create_post, name="createpost"),
    path("profile/<slug>/", views.profile, name="profile"),
    path('likepost/', views.like_post, name='like_post'),
    path('dislikepost/', views.dislike_post, name='dislike_post'),
     #url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
]
