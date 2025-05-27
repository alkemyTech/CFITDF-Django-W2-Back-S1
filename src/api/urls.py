from django.urls import path
from .views import ServicioListaAPIView, ServicioRetrieveAPIView

urlpatterns = [
    path('servicios/', ServicioListaAPIView.as_view(),
         name='api_servicios_lista'),
    path('servicios/<int:pk>',ServicioRetrieveAPIView.as_view(),
         name='api_servicios_detalle')
]
