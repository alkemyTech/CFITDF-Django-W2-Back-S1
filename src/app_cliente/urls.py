from django.urls import path
from .views import ClienteListView

app_name = "app_cliente"

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_lista'),
]
