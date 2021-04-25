from django.contrib import admin
from .models import Like, Post, Topic, Comment

admin.site.register(Post)

admin.site.register(Comment)


admin.site.register(Topic)

admin.site.register(Like)