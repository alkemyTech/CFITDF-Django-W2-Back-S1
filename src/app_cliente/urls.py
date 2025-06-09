from django.urls import path
from .views import (
    ClienteCreateView, ClienteUpdateView,
    ClienteListView, ClienteDeleteView,
    ClienteDetailView
)

app_name = "app_cliente"

urlpatterns = [
    path('crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(),
         name='cliente_update'),
    path('', ClienteListView.as_view(), name='cliente_lista_activos'),
    path('inactivos/', ClienteListView.as_view(),
         {'show_inactive': True}, name='cliente_lista_inactivos'),
    path('borrar/<int:pk>/', ClienteDeleteView.as_view(),
         name="borrar_cliente"),
    path('detalles/<int:pk>/', ClienteDetailView.as_view(),
         name="detalle_servicio"),
]
