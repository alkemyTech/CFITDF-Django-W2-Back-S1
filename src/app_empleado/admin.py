from django.contrib import admin
from .models import Empleado
from webapp.admin_site import custom_admin_site

@admin.register(Empleado, site=custom_admin_site)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'legajo', 'activo')
    list_filter = ('activo',)
    actions = ['dar_de_baja', 'dar_de_alta']
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