from django.contrib import admin
from .models import Videogame, Review, Collection

# Register your models here.
admin.site.register(Videogame)
admin.site.register(Review)
admin.site.register(Collection)