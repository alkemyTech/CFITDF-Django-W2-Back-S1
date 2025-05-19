from django.db import models

# Create your models here.
class CoordinadorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)


class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_documento = models.PositiveIntegerField(unique=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    objects = CoordinadorManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.numero_documento}"
    
    class Meta:
        verbose_name = "Coordinador"
        verbose_name_plural = "Coordinadores"