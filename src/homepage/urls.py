from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('endpoints', views.endpoints, name='endpoints'),
]