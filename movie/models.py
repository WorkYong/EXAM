from platform import release
from turtle import title
from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth = models.DateField(max_length=50)

    # def __str__(self):
    #     return self.first_name
    
    
    class Meta:
        db_table = 'actors'



class Bridge(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    class Meta:
        db_table = 'bridges'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release = models.DateField(max_length=100)
    running_time = models.IntegerField(max_length=20)
    actor = models.ManyToManyField("Actor", through='Bridge')

    #def __str__(self):
        #return self.title
    
    
    class Meta:
        db_table = 'movies'