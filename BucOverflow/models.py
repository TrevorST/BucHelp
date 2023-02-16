from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    #slug is the url
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True)
    
    def __str__(self):
        return (
            f"{self.title}"
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:150]}..."
            f"\n"
        )
class User(models.Model):
    text = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    content  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]
    

class Reply(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]