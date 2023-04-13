from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.utils.timezone import utc
import math

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

    def getKarma(self):
        karma=0
        posts=Post.objects.filter(user=self)
        comments=Comment.objects.filter(user=self)
        for post in posts:
            karma += post.karma
        for comment in comments:
            karma += comment.karma

        self.karma = karma




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
    karma = models.IntegerField(default=0)
    timeElapsed= models.TextField(default="just now")
    #reply_count

    def getTimeElapsed(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - self.created_at
        seconds=math.floor(timediff.total_seconds())

        if seconds < 60:
            self.timeElapsed = str(seconds) + " seconds ago"
        elif seconds < 3600:    #minutes
            minutes = seconds // 60 # // discards fractional remainder
            self.timeElapsed = str(minutes) + " minute ago" if minutes == 1 else str(minutes) + " minutes ago"
        elif seconds < 86400:   #hours
            hours = seconds // 3600
            self.timeElapsed = str(hours) + " hour ago" if hours == 1 else str(hours) + " hours ago"
        else:       #days
            days = seconds // 86400
            self.timeElapsed = str(days) + " day ago" if days == 1 else str(days) + " days ago"


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

    likes = models.ManyToManyField(Author, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(Author, blank=True, related_name='dislikes')
    karma = models.IntegerField(default=0)
    

    def get_total_likes(self):
        return self.likes.count()

    def get_total_dislikes(self):
        return self.dislikes.count()

    def update_karma(self):
        self.karma = self.likes.count() - self.dislikes.count()

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


#class LikePost(models.Model):
    #stores likes in Post
    #related name does a backwards relation from Post back to LikePost
    #basically a Post object with a LikePost object attached to it
#    post = models.OneToOneField(Post, related_name="likes_post", on_delete=models.CASCADE)
#    users = models.ManyToManyField(Author, related_name='requirement_comment_likes')
#    created_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return str(self.post.content)[:30] + " Likes: " +str(self.users.count())