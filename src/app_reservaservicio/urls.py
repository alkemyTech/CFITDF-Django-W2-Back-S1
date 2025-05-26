from django.urls import path
from .views import ReservaServicioCreateView

app_name = "app_reservaservicio"

urlpatterns = [
    path('crear/', ReservaServicioCreateView.as_view(), name='reserva_create'),
]