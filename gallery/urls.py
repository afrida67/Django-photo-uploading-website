
from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    #/gallery/
    path('', views.index, name='index'),
    path('<album_id>',views.detail, name='detail'),
]
 