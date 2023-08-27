from django.db import models

# Create your models here.
class Videogame(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    description = models.TextField
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    date = models.DateField
    platforms = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title
