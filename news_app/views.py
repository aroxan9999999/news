from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import News
from django.views.generic import DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string
from urllib.parse import unquote
from django.db.models import F, Func, Q


def news_view(request):
    news_data = News.objects.all().order_by('-published_at')
    return render(request, 'news/news.html', {'news_data': news_data})


def search(request):
    query = unquote(request.GET.get('q', ''))  # Декодирование параметра запроса
    if query:
        title_results = News.objects.filter(title__icontains=query).order_by('-published_at')
        content_results = News.objects.filter(content__icontains=query).order_by('-published_at')
        results = title_results.union(content_results)
    else:
        results = News.objects.all().order_by('-published_at')

    html = render_to_string('news_search.html', {'news_data': results})
    return HttpResponse(html)
