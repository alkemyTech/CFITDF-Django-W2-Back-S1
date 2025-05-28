from django.db import models


class EmpleadoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

    objects = EmpleadoManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.activo = False
        self.save()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Legajo: {self.legajo} - Activo: {self.activo}'
