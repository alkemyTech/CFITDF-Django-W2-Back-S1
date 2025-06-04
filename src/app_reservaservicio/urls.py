from django.urls import path
from .views import (
    ReservaServicioCreateView, ReservaServicioListView,
    ReservaServicioUpdateView, ReservaServicioDeleteView,
    ReservaServicioDetailView
)


app_name = "app_reservaservicio"

urlpatterns = [
    path('crear/', ReservaServicioCreateView.as_view(), name='reserva_create'),
    path('', ReservaServicioListView.as_view(), name='reserva_lista'),
    path('editar/<int:pk>/', ReservaServicioUpdateView.as_view(),
         name='reserva_update'),
    path('borrar/<int:pk>/', ReservaServicioDeleteView.as_view(),
         name="borrar_reserva"),
    path('detalles/<int:pk>/', ReservaServicioDetailView.as_view(),
         name="detalle_reserva"),
]
