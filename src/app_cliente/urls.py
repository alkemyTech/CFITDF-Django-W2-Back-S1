from django.urls import path
from .views import ClienteCreateView

app_name = 'app_cliente'

urlpatterns = [
    path('crear/', ClienteCreateView.as_view(), name='cliente_create'),
]