from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'legajo', 'activo')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')
    
    def get_queryset(self, request):
        return Empleado.all_objects.all()

    @admin.action(description='Dar de baja empleados seleccionados')
    def dar_de_baja(self, request, queryset):
        queryset.update(activo=False)

    @admin.action(description='Dar de alta empleados seleccionados')
    def dar_de_alta(self, request, queryset):
        queryset.update(activo=True)