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
]
