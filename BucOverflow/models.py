from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dweet(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
class User(models.Model):
    text = models.CharField(max_length=50)
    

