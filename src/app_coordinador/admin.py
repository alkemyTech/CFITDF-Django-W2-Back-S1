from django.contrib import admin
from .models import Coordinador
from webapp.admin_site import custom_admin_site

@admin.register(Coordinador, site=custom_admin_site)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_documento',
                    'fecha_alta', 'activo')
    list_filter = ('activo',)
    actions = ['dar_de_baja', 'dar_de_alta']
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')

    def get_queryset(self, request):
        return Coordinador.all_objects.all()

    @admin.action(description='Dar de baja coordinadores seleccionados')
    def dar_de_baja(self, request, queryset):
        queryset.update(activo=False)

    @admin.action(description='Dar de alta coordinadores seleccionados')
    def dar_de_alta(self, request, queryset):
        queryset.update(activo=True)