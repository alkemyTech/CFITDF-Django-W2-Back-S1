from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre}: {self.descripcion}, {self.precio}'
