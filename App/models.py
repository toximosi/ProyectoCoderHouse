#importaciones-----------------------
from turtle import title
from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    curso = models.IntegerField()
class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    entregables = models.CharField(max_length=10)
    FechaDeInicio = models.DateField()
    FechaDeFin = models.DateField()
    Horario = models.TimeField()

class Entregables(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    FechaEntrega = models.DateField()
    Nota = models.IntegerField()

