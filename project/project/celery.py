import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
 
app = Celery('project')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'weekly_msg': {
        'task': 'board.tasks.weekly_msg',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}