from django.urls import path, include

from . import views
from .views import dashboard

app_name = "BucOverflow"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
