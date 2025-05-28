from django.contrib import admin
from .models import ReservaServicio


@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servicio', 'fecha_evento',
                    'fecha_reserva', 'empleado', 'coordinador')
    list_filter = ('fecha_evento', 'servicio')
    search_fields = ('cliente__nombre', 'cliente__apellido',
                     'servicio__nombre')
