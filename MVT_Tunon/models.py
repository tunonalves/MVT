from django.db import models

# Create your models here.

class family(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    dni = models.IntegerField()