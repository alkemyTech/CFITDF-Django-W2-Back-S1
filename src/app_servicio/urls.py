from django.urls import path
from .views import ServicioCreateView, ServicioListView

app_name = "app_servicio"

urlpatterns = [
    path('crear/', ServicioCreateView.as_view(), name='servicio_create'),
    path('', ServicioListView.as_view(), name='servicio_lista'),
]
