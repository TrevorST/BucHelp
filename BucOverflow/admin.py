from django.contrib import admin
from .models import Post, Comment

# Register your models here.

admin.site.register(Post)

admin.site.register(Comment)

#Generate the slug and just make it the title
#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('title',)}