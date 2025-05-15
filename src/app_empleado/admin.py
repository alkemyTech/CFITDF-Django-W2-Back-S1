from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'legajo', 'activo')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')