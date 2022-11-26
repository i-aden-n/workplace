from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse, reverse_lazy

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=255, null=True)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_manage_url(self):
        return reverse('c_movie', kwargs = {'movie_slug': self.slug})
    
    def get_add_url(self):
        return reverse('add_serial', kwargs = {'movie_slug': self.slug})


class Series(models.Model):
    serial = models.IntegerField(verbose_name='serial number')
    season = models.IntegerField(default=1)
    path = models.FileField(upload_to='videos/%Y/%m/%d')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.movie.name}'
    
    def get_absolute_url(self):
        return reverse('watch', kwargs = {'movie_slug': self.movie.slug, 'season': self.season, 'serial': self.serial})
    
    def get_edit_url(self):
        return reverse('edit_serial', kwargs= {'movie_slug': self.movie.slug, 'season': self.season, 'serial': self.serial})