from django import forms

from .models import Comment, Post


class CreatePostForm(forms.ModelForm):
    content = forms.ImageField()
    caption = forms.CharField(max_length=512, required=False)

    class Meta:
        model = Post
        fields = [
            'content',
            'caption',
        ]


class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = [
            'text',
        ]
