from django.db import models
from django.urls import reverse

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'pk': self.id})

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
    collections = models.ManyToManyField(Collection)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('videogames_detail', kwargs={'videogame_id': self.id})

class Review(models.Model):
    class Rating(models.IntegerChoices):
        R1 = 1,
        R2 = 2,
        R3 = 3,
        R4 = 4,
        R5 = 5
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    videogame = models.ForeignKey(Videogame, related_name="reviews", on_delete=models.CASCADE)

    rating = models.IntegerField(choices=Rating.choices)
    
    def __str__(self):
        return f"{self.name} @ {self.date}"
    
    class Meta:
        ordering = ['-date']
