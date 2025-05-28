from django.urls import path
from .views import (
    CoordinadorCreateView, CoordinadorListView, 
    CoordinadorUpdateView, CoordinadorDeleteView
)

app_name = "app_coordinador"

urlpatterns = [
    path('crear/', CoordinadorCreateView.as_view(), name='coordinador_create'),
    path('', CoordinadorListView.as_view(), name='coordinador_lista'),
    path('editar/<int:pk>/', CoordinadorUpdateView.as_view(),
         name='coordinador_update'),
    path("borrar/<int:pk>/", CoordinadorDeleteView.as_view(),
         name="borrar_coordinador"),
]
