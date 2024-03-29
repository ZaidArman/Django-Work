from django.contrib import admin
from news.models import NewsModel

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_description')
    
# Register your models here.
admin.site.register(NewsModel, NewsAdmin)
