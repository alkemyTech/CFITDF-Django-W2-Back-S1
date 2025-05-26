from django.urls import path
from .views import ServicioCreateView

app_name = "app_servicio"

urlpatterns = [
    path('crear/', ServicioCreateView.as_view(), name='servicio_create'),
]
