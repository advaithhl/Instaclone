from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    content = forms.ImageField()
    caption = forms.CharField(max_length=512)

    class Meta:
        model = Post
        fields = [
            'content',
            'caption',
        ]
