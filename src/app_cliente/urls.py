from django.urls import path
from .views import ClienteCreateView, ClienteUpdateView, ClienteListView, ClienteDeleteView

app_name = "app_cliente"

urlpatterns = [
    path('crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('', ClienteListView.as_view(), name='cliente_lista'),
    path("borrar/<int:pk>/", ClienteDeleteView.as_view(), name="borrar_cliente"),
]
