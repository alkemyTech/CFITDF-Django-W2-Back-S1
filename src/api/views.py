from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from app_servicio.models import Servicio
from app_cliente.models import Cliente
from app_empleado.models import Empleado
from app_coordinador.models import Coordinador
from .serializers import (
    ServicioListaSerializer, ServicioDetalleSerializer,
    ClienteListaSerializer, ClienteDetalleSerializer, 
    EmpleadoListaSerializer, EmpleadoDetalleSerializer,
    CoordinadorListaSerializer, CoordinadorDetalleSerializer
)


class ServicioListaAPIView(APIView):
    def get(self, request):
        servicios = Servicio.objects.filter(activo=True)
        serializer = ServicioListaSerializer(servicios, many=True)
        return Response(serializer.data)


class ServicioRetrieveAPIView(RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioDetalleSerializer


class ClienteListaAPIView(APIView):
    def get(self, request):
        clientes = Cliente.objects.filter(activo=True)
        serializer = ClienteListaSerializer(clientes, many=True)
        return Response(serializer.data)


class ClienteRetrieveAPIView(RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteDetalleSerializer


class EmpleadoListaAPIView(APIView):
    def get(self, request):
        empleados = Empleado.objects.filter(activo=True)
        serializer = EmpleadoListaSerializer(empleados, many=True)
        return Response(serializer.data)


class EmpleadoRetrieveAPIView(RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoDetalleSerializer


class CoordinadorListaAPIView(APIView):
    def get(self, request):
        coordinadores = Coordinador.objects.filter(activo=True)
        serializer = CoordinadorListaSerializer(coordinadores, many=True)
        return Response(serializer.data)


class CoordinadorRetrieveAPIView(RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorDetalleSerializer
