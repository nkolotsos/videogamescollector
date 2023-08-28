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
        return reverse('videogames_detail', kwargs={'videogames_id': self.id})

class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    videogame = models.ForeignKey(Videogame, related_name="reviews", on_delete=models.CASCADE)

    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES, default=3)

    def __str__(self):
        return f"{self.name} @ {self.date}"
    
    def get_absolute_url(self):
        return reverse('add_review', kwargs={'videogame_id': self.id})

    @property
    def rating_display(self):
        return dict(self.RATING_CHOICES).get(self.rating)
    
    class Meta:
        ordering = ['-date']