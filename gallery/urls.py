##list of urls for music section
from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
]
 