from django.urls import path
from .views import EmpleadoCreateView

app_name = "app_empleado"

urlpatterns = [
    path('crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
]