from django.contrib import admin
from .models import Videogame, Review

# Register your models here.
admin.site.register(Videogame)
admin.site.register(Review)