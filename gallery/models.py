from django.db import models

# Create your models here.

class Album(models.Model):
    caption = models.CharField(max_length=500)
    hashtag = models.CharField(max_length=100)
    photo = models.FileField()
