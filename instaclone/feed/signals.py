from os import remove as os_remove

from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Post


@receiver(post_delete, sender=Post)
def delete_content_file(instance: Post, **kwargs):
    content_file = instance.content.path
    os_remove(content_file)
