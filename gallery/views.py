from django.shortcuts import render
from . models import Album
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>hi this works")
   