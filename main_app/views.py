from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Videogame, Review, Collection
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def videogames_index(request):
    videogames = Videogame.objects.all()
    return render(request, 'videogames/index.html', { 'videogames': videogames })

def videogames_detail(request, videogame_id):
    videogame = Videogame.objects.get(id=videogame_id)
    id_list = videogame.collections.all().values_list('id')
    not_included = Collection.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'videogames/detail.html', { 'videogame': videogame, 'review_form': review_form, 'collections': not_included})

def add_review(request, videogame_id):
    form = ReviewForm(request.POST)
    print(videogame_id)
    if form.is_valid():
        review = form.save(commit=False)
        print(review.videogame_id)
        review.videogame_id = videogame_id
        review.save()
    else:
        print(form.errors)
    return redirect('videogames_detail', videogame_id=videogame_id)

class VideogameCreate(CreateView):
    model = Videogame
    fields = ['title', 'genres']
    success_url = '/videogames'

class VideogameUpdate(UpdateView):
    model = Videogame
    fields = [
        'genres', 'description', 'developer', 'publisher', 'platforms'
        ]

class VideogameDelete(DeleteView):
    model = Videogame
    success_url = '/videogames'
    template_name = 'main_app/videogame_confirm_delete.html'

class CollectionList(ListView):
    model = Collection

class CollectionDetail(DetailView):
    model = Collection

class CollectionCreate(CreateView):
    model = Collection
    fields = ['name']
    success_url = 'collections/'

class CollectionUpdate(UpdateView):
    model = Collection
    fields = ['name']

class CollectionDelete(DeleteView):
    model = Collection
    success_url = '/collections'

def assoc_collection(request, videogame_id, collection_id):
    Videogame.objects.get(id=videogame_id).collections.add(collection_id)
    return redirect('videogames_detail', videogame_id=videogame_id)

def unassoc_collection(request, videogame_id, collection_id):
    Videogame.objects.get(id=videogame_id).collections.remove(collection_id)
    return redirect('videogames_detail', videogame_id=videogame_id)

