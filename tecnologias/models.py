# from typing_extensions import Required
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class articulo(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField()
    autor = models.CharField(max_length=50)
    referencias = models.TextField(max_length=500)
    fechaPublicacion = models.DateTimeField(default=datetime.now())
    fechaActualizacion = models.DateTimeField()
