from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model
from .models import Post


class PostUploadForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        #print("this entire process happened")




class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']

