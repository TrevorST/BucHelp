from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.text import slugify
try:
    User = settings.AUTH_USER_MODEL
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User


# Create your models here.





class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content  = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]
    

class Post(models.Model):
    title = models.CharField(max_length=100, default='no title')
    #slug is the url
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField(blank=True, default='')
    body = models.TextField(max_length=10000, default='') #delete
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.title}"
            f"{self.user} "
            f"{self.body[:30]}..."
        )


    def get_url(self):
        return reverse("post", kwargs={
            "slug":self.slug
        })


