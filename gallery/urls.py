
from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    #/gallery/
    path('', views.IndexView.as_view(), name='index'), #consider that class as_view
    path('<pk>',views.DetailView.as_view(), name='detail'),
    # /gallery/album/add
    path('album/add',views.AlbumCreate.as_view(), name='album-add'),
    # /gallery/album/1/delete
    path('album<pk>/delete',views.AlbumDelete.as_view(), name='album-delete'),
]
 