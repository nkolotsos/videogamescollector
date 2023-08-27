from django.shortcuts import render
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

