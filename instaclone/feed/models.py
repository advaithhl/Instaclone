from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .utils import pad_image


def _user_content_dir(instance, filename):
    return f'{instance.creator.username}/{filename}'


class Post(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=512, blank=True)
    liked_users = models.ManyToManyField(
        User, related_name='likes', blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    content = models.ImageField(
        upload_to=_user_content_dir,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        pad_image(self.content).save(self.content.path)


class Comment(models.Model):
    # Setting the comment to delete if author is deleted, for now.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
