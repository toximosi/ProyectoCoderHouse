#importaciones-----------------------
from turtle import title
from django.db import models

# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=100)