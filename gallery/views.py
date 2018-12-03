from django.shortcuts import render
from . models import Album
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    all_photos = Album.objects.all() 
    return render(request, 'gallery/index.html', {'all_photos' : all_photos})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'gallery/detail.html', {'album' : album})
   