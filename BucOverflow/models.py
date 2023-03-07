from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

##broken

@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance, slug=slugify(instance.username), fullname=instance.first_name+instance.last_name)

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = models.TextField(blank=True,max_length=10000, default='Welcome to my page!')
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Reply(models.Model):
    #default poster is anon
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.content[:100]


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content  = models.TextField(blank=True,max_length=10000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)
    #reply_count

    def __str__(self):
        return self.content[:100]
    

class Post(models.Model):
    title = models.CharField(max_length=100, default='no title')
    #slug is the url
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(blank=True,max_length=10000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return (
            #f"{self.title}"
            #f"{self.user} "
            f"{self.content[:30]}..."
        )


    def get_url(self):
        return reverse("post", kwargs={
            "slug":self.slug
        })


