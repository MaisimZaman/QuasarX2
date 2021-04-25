from django import forms
from django.contrib.auth.models import User
from django.forms.models import fields_for_model
from public_chat.models import PublicChatRoom


class ChatUploadForm(forms.ModelForm):

    class Meta:
        model = PublicChatRoom
        fields = ['title', 'discription', 'max_members']
