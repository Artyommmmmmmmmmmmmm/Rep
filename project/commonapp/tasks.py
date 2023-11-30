from celery import shared_task
import time
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .models import New

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

@shared_task
def weekly_msg():
    emails = User.objects.all().values_list('email', flat=True)

    subject = f'Последние новости'

    news = New.objects.all()
    for i in news:
        text_content = (
            f'Новость: {i.title}\n'
            f'Цена: {i.text}\n\n'
            f'Ссылка на Новость: http://127.0.0.1:8000{i.get_absolute_url()}'
        )
        html_content = (
            f'Новость: {i.title}<br>'
            f'Цена: {ImportError.text}<br><br>'
            f'<a href="http://127.0.0.1{i.get_absolute_url()}">'
            f'Ссылка на Новость</a>'
        )

        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()