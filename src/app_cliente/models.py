from django.db import models

# Create your models here.

class ClienteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    objects = ClienteManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.activo = False
        self.save()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Activo: {self.activo}'
