from django.contrib import admin
from .models import Cliente
from webapp.admin_site import custom_admin_site

@admin.register(Cliente, site=custom_admin_site)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'activo')
    list_filter = ('activo',)
    actions = ['dar_de_baja', 'dar_de_alta']
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')

    def get_queryset(self, request):
        return Cliente.all_objects.all()

    @admin.action(description='Dar de baja clientes seleccionados')
    def dar_de_baja(self, request, queryset):
        queryset.update(activo=False)

    @admin.action(description='Dar de alta clientes seleccionados')
    def dar_de_alta(self, request, queryset):
        queryset.update(activo=True)