from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from app_servicio.models import Servicio
from app_cliente.models import Cliente
from .serializers import ServicioSerializer

class ServicioListaAPIView(APIView):
    def get(self, request):
        nombres = list(Servicio.objects.filter(
            activo=True).values_list('nombre', flat=True))
        return Response(nombres)
    
class ServicioRetrieveAPIView(RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ClienteListaAPIView(APIView):
    def get(self, request):
        nombres_apellidos = list(Cliente.objects.filter(
            activo=True).values_list('nombre', 'apellido'))
        return Response(nombres_apellidos)