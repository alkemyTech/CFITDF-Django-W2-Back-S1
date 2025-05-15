from django.db import models
from app_coordinador.models import Coordinador
from app_cliente.models import Cliente
from app_servicio.models import Servicio
from app_empleado.models import Empleado

class ReservaServicio(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_evento = models.DateTimeField()

    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
    )

    servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE,
    )
    
    empleado = models.ForeignKey(
        Empleado, 
        on_delete=models.SET_NULL,
        null=True,
    )
    
    coordinador = models.ForeignKey(
        Coordinador, 
        on_delete=models.SET_NULL,
        null=True,
    )
    
    def __str__(self):
        return f"Reserva de {self.cliente} para {self.servicio} el {self.fecha_evento.strftime('%Y-%m-%d')}"
