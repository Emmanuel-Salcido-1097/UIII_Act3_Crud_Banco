from django.db import models

# Create your models here.

class Sucursales(models.Model):
    Id_Sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ubicacion  = models.CharField(max_length=100)
    tamaño   = models.FloatField()
    encargado = models.CharField(max_length=100)
    horarios  = models.TimeField()
    capacidad =  models.IntegerField()

    class Meta: 
        db_table =  "Sucursales"
        verbose_name = "Sucursale"
        verbose_name_plural = "Sucursales"

    def   __str__(self):
        return self.nombre