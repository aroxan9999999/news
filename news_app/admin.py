from django.contrib import admin
from .models import News
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'display_image')
    search_fields = ('title', 'content')

    def display_image(self, obj):
        if obj.url_to_image:
            return mark_safe('<img src="{}" width="150" height="auto" />'.format(obj.url_to_image))
        return ""

    display_image.short_description = 'Image'
    display_image.allow_tags = True


admin.site.register(News, NewsAdmin)
