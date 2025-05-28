from django.contrib import admin
from .models import Servicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'activo')
    list_filter = ('activo',)
    actions = ['dar_de_baja', 'dar_de_alta']
    search_fields = ('nombre',)
    ordering = ('nombre',)

    def get_queryset(self, request):
        return Servicio.all_objects.all()

    @admin.action(description='Dar de baja servicios seleccionados')
    def dar_de_baja(self, request, queryset):
        queryset.update(activo=False)

    @admin.action(description='Dar de alta servicios seleccionados')
    def dar_de_alta(self, request, queryset):
        queryset.update(activo=True)
