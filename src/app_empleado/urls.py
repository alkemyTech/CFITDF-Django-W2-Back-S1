from django.urls import path
from .views import EmpleadoCreateView, EmpleadoListView

app_name = "app_empleado"

urlpatterns = [
    path('crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('', EmpleadoListView.as_view(), name='empleado_lista'),
]