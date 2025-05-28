from django.urls import path
from .views import (
    ServicioListaAPIView, ServicioRetrieveAPIView,
    ClienteListaAPIView, ClienteRetrieveAPIView,
    EmpleadoListaAPIView, EmpleadoRetrieveAPIView,
    CoordinadorListaAPIView, CoordinadorRetrieveAPIView
)


urlpatterns = [
    path('servicios/', ServicioListaAPIView.as_view(),
         name='api_servicios_lista'),
    path('servicios/<int:pk>', ServicioRetrieveAPIView.as_view(),
         name='api_servicios_detalle'),
    path('clientes/', ClienteListaAPIView.as_view(),
         name='api_clientes_lista'),
    path('clientes/<int:pk>', ClienteRetrieveAPIView.as_view(),
         name='api_clientes_detalle'),
    path('empleados/', EmpleadoListaAPIView.as_view(),
         name='api_empleados_lista'),
    path('empleados/<int:pk>', EmpleadoRetrieveAPIView.as_view(),
         name='api_empleados_detalle'),
    path('coordinadores/', CoordinadorListaAPIView.as_view(),
         name='api_coordinadores_lista'),
    path('coordinadores/<int:pk>', CoordinadorRetrieveAPIView.as_view(),
         name='api_coordinadores_detalle'),
]
