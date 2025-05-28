from django.db import models


class ServicioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

    objects = ServicioManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.activo = False
        self.save()

    def __str__(self):
        return f'{self.nombre}: {self.descripcion}, {self.precio}'
