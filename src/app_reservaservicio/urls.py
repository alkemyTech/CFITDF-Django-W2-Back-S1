from django.urls import path
from .views import ReservaServicioCreateView, ReservaServicioListView

app_name = "app_reservaservicio"

urlpatterns = [
    path('crear/', ReservaServicioCreateView.as_view(), name='reserva_create'),
    path('', ReservaServicioListView.as_view(), name='reserva_lista'),
]