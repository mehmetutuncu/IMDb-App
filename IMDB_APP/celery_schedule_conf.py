from __future__ import absolute_import

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'top_250_movies': {
        'task': 'movies.tasks.top_250_movies',
        # 'schedule': crontab(hour="*/1"),
        'schedule': 60,
        'args': (),
    },
    'most_popular_movies': {
        'task': 'movies.tasks.most_popular_movies',
        # 'schedule': crontab(hour="*/1"),
        'schedule': 60,
        'args': (),
    },
    'top_250_tv_shows': {
        'task': 'tv_shows.tasks.top_250_tv_shows',
        # 'schedule': crontab(hour="*/1"),
        'schedule': 60,
        'args': (),
    },
    'most_popular_tv_shows': {
        'task': 'tv_shows.tasks.most_popular_tv_shows',
        # 'schedule': crontab(hour="*/1"),
        'schedule': 60,
        'args': (),
    },
}
