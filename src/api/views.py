from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app_servicio.models import Servicio


class ServicioListaAPIView(APIView):
    def get(self, request):
        nombres = list(Servicio.objects.filter(
            activo=True).values_list('nombre', flat=True))
        return Response(nombres)
