from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from IMDB_APP.celery_schedule_conf import CELERYBEAT_SCHEDULE

# set the default Django settings module for the 'celery' program.
os.environ['DJANGO_SETTINGS_MODULE'] = 'IMDB_APP.settings'
app = Celery('IMDB_APP')

app.config_from_object('django.conf:settings')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
task_apps = ['IMDB_APP.movies']

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS + task_apps)

CELERY_IMPORTS = ('IMDB_APP.movies.tasks')

app.conf.beat_schedule = CELERYBEAT_SCHEDULE


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))