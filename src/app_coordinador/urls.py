from django.urls import path
from .views import CoordinadorCreateView

app_name = "app_coordinador"

urlpatterns = [
    path('crear/', CoordinadorCreateView.as_view(), name='coordinador_create'),
]