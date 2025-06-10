from django.contrib import admin
from .models import ReservaServicio
from webapp.admin_site import custom_admin_site

@admin.register(ReservaServicio, site=custom_admin_site)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servicio', 'fecha_evento',
                    'fecha_reserva', 'empleado', 'coordinador')
    list_filter = ('fecha_evento', 'servicio')