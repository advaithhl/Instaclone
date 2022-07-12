import os

from django.core.mail import send_mail
from django.template import loader


def send_welcome_mail(firstname, username, email_address):
    html_template = loader.get_template('communication/email_welcome.html')
    context = {
        'firstname': firstname,
        'username': username,
    }
    html = html_template.render(context)

    text = f"""
    Hi {firstname},

    You are receiving this email because you had signed up for Instaclone as
    {username}.

    Have a great day!
    Team Instaclone
    """

    subject = "Welcome to Instaclone!"
    from_email = os.getenv('INSTACLONE_MAIL_USER')
    to_email = [email_address]

    send_mail(
        subject=subject,
        message=text,
        from_email=from_email,
        recipient_list=to_email,
        html_message=html,
    )
