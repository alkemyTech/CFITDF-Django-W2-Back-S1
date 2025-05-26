from django.urls import path
from .views import ClienteCreateView
from .views import ClienteListView

app_name = "app_cliente"

urlpatterns = [
    path('crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('', ClienteListView.as_view(), name='cliente_lista'),
]