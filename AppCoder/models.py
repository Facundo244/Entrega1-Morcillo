from django.db import models

# Create your models here.
class Sector(models.Model):

    nombre=models.CharField(max_length=40)

class Profesional(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Turno(models.Model):
    nombre= models.CharField(max_length=30)
    turnoDeTrabajo = models.TimeField()  

