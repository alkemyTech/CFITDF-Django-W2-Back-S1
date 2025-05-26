from django.urls import path
from .views import ReservaServicioCreateView, ReservaServicioListView, ReservaServicioUpdateView

app_name = "app_reservaservicio"

urlpatterns = [
    path('crear/', ReservaServicioCreateView.as_view(), name='reserva_create'),
    path('', ReservaServicioListView.as_view(), name='reserva_lista'),
    path('editar/<int:pk>/', ReservaServicioUpdateView.as_view(), name='reserva_update'),
]