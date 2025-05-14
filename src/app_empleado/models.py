from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Legajo: {self.legajo} - Activo: {self.activo}'