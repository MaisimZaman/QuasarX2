from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from PIL import Image
from django import forms
from django.utils.functional import LazyObject

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    #video = models.FileField(upload_to='videos')
    video_link = models.CharField(default=None, max_length=200)
    #discription = models.TextField(null=True)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.CharField(default='undefined', max_length=100)
    type = models.CharField(default='video_posts', max_length=20)
    discription = models.TextField(default='', max_length=10000)
    views = models.IntegerField(default=0)
    
    @property
    def use_link(self):
        final = str(self.video_link).replace("watch?v=", "embed/")
        return final 


    def add_view(self):
        self.views += 1
        self.save()



    def __str__(self):
        return str(self.title)



class OVideo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos')
    date_posted = models.DateField(default=timezone.now)
    discription = models.TextField()


    def __str__(self):
        return str(self.title)



