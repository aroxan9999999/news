from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'fetch_news_every_10_seconds': {
        'task': 'news_app.tasks.fetch_news',
        'schedule': timedelta(seconds=10),
    },
}
