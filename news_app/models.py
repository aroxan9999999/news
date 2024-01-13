from django.db import models
from django.urls import reverse


class News(models.Model):
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500)
    url_to_image = models.URLField(null=True, blank=True, max_length=500)
    published_at = models.DateTimeField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

