from django.urls import path
from .views import ServicioCreateView, ServicioListView, ServicioUpdateView

app_name = "app_servicio"

urlpatterns = [
    path('crear/', ServicioCreateView.as_view(), name='servicio_create'),
    path('', ServicioListView.as_view(), name='servicio_lista'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(), name='servicio_update'),
]
