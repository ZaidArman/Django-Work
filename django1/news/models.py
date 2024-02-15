from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class NewsModel(models.Model):
    news_title = models.CharField(max_length=100)
    news_description = HTMLField()
