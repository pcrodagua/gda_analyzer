from django.db import models

class Producto(models.Model):
    nombre = models.CharField(unique=False, max_length=200)
    grasa_saturada = models.IntegerField()
    otras_grasas  = models.IntegerField()
    azucar_total = models.IntegerField()
    sodio = models.IntegerField()
    energia = models.IntegerField()