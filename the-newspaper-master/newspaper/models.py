from django.db import models

# Create your models here.
class News(models.Model):
    source = models.CharField(max_length=100)
    issue = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    news_title = models.CharField(max_length=250)
    news_image = models.CharField(max_length=250)
    news_content = models.TextField()

    def __str__(self):
        return self.news_title
