from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    
    caption = models.TextField()
    photo = models.FileField()
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
   # photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.caption
    
    def total_likes(self):
        return self.likes.count() 

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={"album_id": self.pk})