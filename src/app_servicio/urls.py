from django.urls import path
from .views import (
    ServicioCreateView, ServicioListView,
    ServicioUpdateView, ServicioDeleteView,
    ServicioDetailView
)

app_name = "app_servicio"

urlpatterns = [
    path('crear/', ServicioCreateView.as_view(), name='servicio_create'),
    path('', ServicioListView.as_view(), name='servicio_lista'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(),
         name='servicio_update'),
    path('borrar/<int:pk>/', ServicioDeleteView.as_view(),
         name="borrar_servicio"),
    path('detalles/<int:pk>/', ServicioDetailView.as_view(),
         name="detalle_servicio"),
]
