from django.db import models

# Create your models here.
class productos(models.Model):
    producto = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 30)
    precio = models.IntegerField()
    
class categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 30)