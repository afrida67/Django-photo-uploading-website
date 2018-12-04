from django.views import generic
from . models import Album
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    # by default  context_object_name is object_list
    context_object_name = 'all_photos'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
        model = Album
        template_name = 'gallery/detail.html'

class AlbumCreate(CreateView):
        model = Album
        fields = ['caption', 'hashtag', 'photo']

class AlbumDelete(DeleteView):
        model = Album
        success_url = reverse_lazy('gallery:index')
        









