from django.contrib import admin
from .models import Coordinador

# Register your models here.

@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_documento', 'fecha_alta', 'activo')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')
