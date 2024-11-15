from django.db import models

# Create your models here.

class Seguridad_Privada(models.Model):
    Id_Seguridad = models.IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=50)
    contacto = models.IntegerField()
    horarios  = models.TimeField()
    personal  = models.IntegerField()
    vehiculos   = models.IntegerField()
    servicios   = models.CharField(max_length=100)

    class Meta: 
        db_table =  "Seguridad_Privada"
        verbose_name = "Seguridad Privada"
        verbose_name_plural = "Seguridad Privada"

    def   __str__(self):
        return self.nombre