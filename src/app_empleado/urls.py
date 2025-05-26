from django.urls import path
from .views import EmpleadoCreateView, EmpleadoListView, EmpleadoUpdateView, EmpleadoDeleteView

app_name = "app_empleado"

urlpatterns = [
    path('crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('', EmpleadoListView.as_view(), name='empleado_lista'),
    path('editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path("borrar/<int:pk>/", EmpleadoDeleteView.as_view(), name="borrar_empleado"),
]