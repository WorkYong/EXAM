from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField(max_length=20)
    
    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    age = models.IntegerField(max_length=20)
    
    class Meta:
        db_table = 'dogs'


