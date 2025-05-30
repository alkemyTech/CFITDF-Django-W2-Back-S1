"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('app_cliente.urls', namespace='app_cliente')),
    path('empleados/', include('app_empleado.urls', namespace='app_empleado')),
    path('servicios/', include('app_servicio.urls', namespace='app_servicio')),
    path('coordinadores/', include('app_coordinador.urls',
         namespace='app_coordinador')),
    path('reservas/', include('app_reservaservicio.urls',
         namespace='app_reservaservicio')),
    path('api/', include('api.urls')),
]
