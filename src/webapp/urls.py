from django.urls import path, include
from webapp.admin_site import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('clientes/', include('app_cliente.urls', namespace='app_cliente')),
    path('coordinadores/', include('app_coordinador.urls',
         namespace='app_coordinador')),
    path('empleados/', include('app_empleado.urls', namespace='app_empleado')),
    path('servicios/', include('app_servicio.urls', namespace='app_servicio')),
    path('reservas/', include('app_reservaservicio.urls',
         namespace='app_reservaservicio')),
    path('api/', include('api.urls')),
    path('', include('homepage.urls')),
]
