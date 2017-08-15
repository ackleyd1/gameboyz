from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('gameboyz')

from celery.schedules import crontab
app.conf.beat_schedule = {
    'update-sales': {
        'task': 'updatesales',
        'schedule': crontab(minute=0, hour=0),
        'args': (),
    },
}

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)