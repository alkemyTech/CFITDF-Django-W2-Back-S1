from rest_framework import serializers
from app_servicio.models import Servicio
from app_cliente.models import Cliente
from app_empleado.models import Empleado
from app_coordinador.models import Coordinador


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'
