from django import forms
from django.contrib.auth.models import User
from django.forms.models import fields_for_model
from .models import Video


class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'video_link', 'discription']
        #print("this entire process happened")
