from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('videogames/', views.videogames_index, name='videogames_index'),
    path('videogames/<int:videogames_pk>/', views.videogames_detail, name='videogames_detail'),
]