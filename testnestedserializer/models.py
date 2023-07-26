from django.db import models

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genre
    
    
class Movie(models.Model):
    name = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.name
    
