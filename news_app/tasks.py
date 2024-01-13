from celery import shared_task
from .models import News
from .news_api import get_news
from django.utils.dateparse import parse_datetime


@shared_task
def fetch_news():
    news_data = get_news()

    for news in news_data['articles']:
        published_at = parse_datetime(news['publishedAt'])

        News.objects.update_or_create(
            title=news['title'],
            defaults={
                'source_name': news['source']['name'],
                'author': news['author'],
                'description': news['description'],
                'url': news['url'],
                'url_to_image': news['urlToImage'],
                'published_at': published_at,
                'content': news['content']
            }
        )
