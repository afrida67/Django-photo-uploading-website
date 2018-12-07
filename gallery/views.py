from django.views import generic
from . models import Album
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    # by default  context_object_name is object_list
    context_object_name = 'all_photos'

    def get_queryset(self):
        return Album.objects.all().order_by('-date')

class DetailView(generic.DetailView):
        model = Album
        template_name = 'gallery/detail.html'

class AlbumDelete(DeleteView):
        model = Album
        success_url = reverse_lazy('gallery:index')

@login_required(login_url="/accounts/login/") #means after logged in, user can see

def album_create(request):
      if request.method == "POST":
            form = forms.CreatePhoto(request.POST, request.FILES)
            if form.is_valid():
                  #save photos to db
                  instance = form.save(commit=False)
                  instance.uploader = request.user
                  instance.save()
                  return redirect('gallery:index')
      else:
             form = forms.CreatePhoto()
      return render(request,'gallery/upload.html',{'form':form})
