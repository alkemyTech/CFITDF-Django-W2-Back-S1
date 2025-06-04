from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('clientes/', include('app_cliente.urls', namespace='app_cliente')),
    path('empleados/', include('app_empleado.urls', namespace='app_empleado')),
    path('servicios/', include('app_servicio.urls', namespace='app_servicio')),
    path('coordinadores/', include('app_coordinador.urls',
         namespace='app_coordinador')),
    path('reservas/', include('app_reservaservicio.urls',
         namespace='app_reservaservicio')),
    path('api/', include('api.urls')),
]
