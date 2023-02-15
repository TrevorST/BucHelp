from django.urls import path, include

from . import views
from .views import base, index, discussions, home

app_name = "BucOverflow"

urlpatterns = [
<<<<<<< Updated upstream
    path("", views.dashboard, name="dashboard"),
=======
    path("", views.base, name="base"),
    path("index", views.index, name="index"),
    path("discussions", views.discussions),
    path("home", views.home, name="home"),
>>>>>>> Stashed changes
]
