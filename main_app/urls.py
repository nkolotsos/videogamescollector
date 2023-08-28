from django.urls import path
from . import views
# from main_app.views import VideogamesListView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('videogames/', views.videogames_index, name='videogames_index'),
    path('videogames/<int:videogame_id>/', views.videogames_detail, name='videogames_detail'),
    path('videogames/create/', views.VideogameCreate.as_view(), name='videogames_create'),
    path('videogames/<int:pk>/update/', views.VideogameUpdate.as_view(), name='videogames_update'),
    path('videogames/<int:pk>/delete/', views.VideogameDelete.as_view(), name='videogames_delete'),
    path('videogames/<int:videogame_id>/add_review', views.add_review, name='add_review'),
    path('videogames/<int:videogame_id>/assoc_collection/<int:collection_id>/', views.assoc_collection, name='assoc_collection'),
    path('videogames/<int:videogame_id>/unassoc_collection/<int:collection_id>/', views.unassoc_collection, name='unassoc_collection'),
    path('collections/', views.CollectionList.as_view(), name='collections_index'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection_detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]
