from xml.etree.ElementTree import Comment
from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'body'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug']