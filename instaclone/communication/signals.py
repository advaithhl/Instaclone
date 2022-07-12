from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import task_send_welcome_mail


@receiver(post_save, sender=User)
def user_model_saved(sender, instance, created, **kwargs):
    if created:
        firstname = instance.first_name
        username = instance.username
        email_address = instance.email
        task_send_welcome_mail.delay(
            firstname=firstname,
            username=username,
            email_address=email_address)
