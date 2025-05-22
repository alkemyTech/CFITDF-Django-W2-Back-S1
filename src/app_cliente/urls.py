from django.urls import path
from .views import ClienteDeleteView

app_name = "app_cliente"

urlpatterns = [
    path("borrar/<int:pk>/", ClienteDeleteView.as_view(), name="borrar_cliente"),
]
