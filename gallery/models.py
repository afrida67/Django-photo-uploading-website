from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    
    caption = models.TextField()
    photo = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
   # photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={"pk": self.pk})
