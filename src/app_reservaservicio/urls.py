from django.urls import path
from .views import ReservaServicioCreateView, ReservaServicioListView, ReservaServicioUpdateView, ReservaServicioDeleteView

app_name = "app_reservaservicio"

urlpatterns = [
    path('crear/', ReservaServicioCreateView.as_view(), name='reserva_create'),
    path('', ReservaServicioListView.as_view(), name='reserva_lista'),
    path('editar/<int:pk>/', ReservaServicioUpdateView.as_view(), name='reserva_update'),
    path("borrar/<int:pk>/", ReservaServicioDeleteView.as_view(), name="borrar_reserva"),
]