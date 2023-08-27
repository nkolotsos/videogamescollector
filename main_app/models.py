from django.db import models
from django.urls import reverse

# Create your models here.
class Videogame(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    # release_date = models.DateField()
    # date = models.DateField()
    platforms = models.CharField(max_length=100)
    # rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('videogames_detail', kwargs={'videogame_id': self.id})

