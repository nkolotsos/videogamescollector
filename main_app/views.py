from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Videogame

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def videogames_index(request):
    videogames = Videogame.objects.all()
    return render(request, 'videogames/index.html', { 'videogames': videogames })

def videogames_detail(request, videogames_id):
    videogame = Videogame.objects.get(id=videogames_id)
    return render(request, 'videogames/detail.html', { 'videogame': videogame })

class VideogameCreate(CreateView):
    model = Videogame
    fields = ['title', 'genres']

class VideogameUpdate(UpdateView):
    model = Videogame
    fields = [
        'genres', 'description', 'developer', 'publisher', 'platforms'
        ]

class VideogameDelete(DeleteView):
    model = Videogame
    success_url = '/videogames'
    template_name = 'main_app/videogame_confirm_delete.html'