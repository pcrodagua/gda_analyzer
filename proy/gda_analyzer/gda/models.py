from django.db import models


class Producto(models.Model):
    nombre = models.CharField(unique=False)
    descripcion = models.CharField(unique=False)
    grasa_saturada = models.IntegerField()
    otras_grasas = models.IntegerField()
    azucar_total = models.IntegerField()
    sodio = models.IntegerField()
    energia = models.IntegerField()
    energia_pporcion = models.IntegerField()
    porcion = models.IntegerField()
