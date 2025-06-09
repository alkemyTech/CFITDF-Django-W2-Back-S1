from django.urls import path
from .views import (
    CoordinadorCreateView, CoordinadorListView,
    CoordinadorUpdateView, CoordinadorDeleteView,
    CoordinadorDetailView
)

app_name = "app_coordinador"

urlpatterns = [
    path('crear/', CoordinadorCreateView.as_view(), name='coordinador_create'),
    path('', CoordinadorListView.as_view(), name='coordinador_lista_activos'),
    path('inactivos/', CoordinadorListView.as_view(),
         {'show_inactive': True}, name='coordinador_lista_inactivos'),
    path('editar/<int:pk>/', CoordinadorUpdateView.as_view(),
         name='coordinador_update'),
    path('borrar/<int:pk>/', CoordinadorDeleteView.as_view(),
         name="borrar_coordinador"),
    path('detalles/<int:pk>/', CoordinadorDetailView.as_view(),
         name="detalle_coordinador"),
]
