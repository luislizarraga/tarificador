from django.db import models

# Create your models here.

class Llamada(models.Model)
    duracion = models.DateTimeField("Duracion de llamada")
    num_marcado = models.IntegerField(max_length = 200)
    destino = models.CharField(max_length = 200)
    costo = models.IntegerField(max_length = 200)
    fecha_llamada = models.DateTimeField('Fecha de llamada')
    num_origen = models.IntegerField(max_length = 200)


