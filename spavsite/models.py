from django.db import models

# Create your models here.

class LatestNews(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='latest_news_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title