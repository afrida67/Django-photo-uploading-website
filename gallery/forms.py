from django import forms
from . import models

class CreatePhoto(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = ['caption', 'photo']