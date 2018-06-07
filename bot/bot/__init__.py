from __future__ import absolute_import, unicode_literals


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from bot.celery import app as celery_app
import os

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bot.settings'
import django
django.setup()

__all__ = ['celery_app']