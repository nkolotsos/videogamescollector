from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Videogame, Review
from .forms import ReviewForm

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
    review_form = ReviewForm()
    return render(request, 'videogames/detail.html', { 'videogame': videogame, 'reivew_form': review_form})

def add_review(request, videogames_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.videogames_id = videogames_id
        review.save()
    return redirect('videogames_detail', videogames_id=videogames_id)

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

