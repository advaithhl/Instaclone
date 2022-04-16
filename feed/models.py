from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def _user_content_dir(instance, filename):
    return f'{instance.creator.username}/{filename}'


class Post(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=512)
    liked_users = models.ManyToManyField(User, related_name='likes')
    time_created = models.DateTimeField(default=timezone.now)
    content = models.ImageField(
        default='placeholder.png',
        upload_to=_user_content_dir,
    )


class Comment(models.Model):
    # Setting the comment to delete if author is deleted, for now.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
