from django.urls import path
from .views import ServicioListaAPIView, ServicioRetrieveAPIView, ClienteListaAPIView, ClienteRetrieveAPIView

urlpatterns = [
    path('servicios/', ServicioListaAPIView.as_view(),
         name='api_servicios_lista'),
    path('servicios/<int:pk>', ServicioRetrieveAPIView.as_view(),
         name='api_servicios_detalle'),
    path('clientes/', ClienteListaAPIView.as_view(), name='api_clientes_lista'),
    path('clientes/<int:pk>', ClienteRetrieveAPIView.as_view(),
         name='api_clientes_detalle'),
]
