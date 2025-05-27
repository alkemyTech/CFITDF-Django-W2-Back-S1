from django.urls import path
from .views import ServicioListaAPIView

urlpatterns = [
    path('servicios/', ServicioListaAPIView.as_view(),
         name='api_servicios_lista'),
]
