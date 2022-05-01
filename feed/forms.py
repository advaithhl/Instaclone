from django import forms
from .models import Post


class CreatePostForm(forms.Form):
    content = forms.ImageField()
