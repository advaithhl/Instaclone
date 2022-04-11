from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .emails import send_welcome_mail


@receiver(post_save, sender=User)
def user_model_saved(sender, instance, created, **kwargs):
    if created:
        firstname = instance.first_name
        username = instance.username
        email_address = instance.email
        send_welcome_mail(
            firstname=firstname,
            username=username,
            email_address=email_address)
