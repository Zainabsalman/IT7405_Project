from django.db import models
from djongo import models

# Create your models here
class App(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)
    

