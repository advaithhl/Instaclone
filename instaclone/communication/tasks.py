from celery import shared_task

from .emails import send_welcome_mail


@shared_task
def task_send_welcome_mail(firstname, username, email_address):
    send_welcome_mail(firstname, username, email_address)
