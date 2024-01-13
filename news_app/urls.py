from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_view, name='news'),
    path('search/', views.search,  name='news_search'),
]
