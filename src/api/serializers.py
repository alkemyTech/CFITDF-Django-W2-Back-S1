from rest_framework import serializers
from app_servicio.models import Servicio
from app_cliente.models import Cliente
from app_empleado.models import Empleado
from app_coordinador.models import Coordinador


class ServicioListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre']


class ServicioDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


class ClienteListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido']


class ClienteDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre', 'apellido']


class EmpleadoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class CoordinadorListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = ['id', 'nombre', 'apellido']


class CoordinadorDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'
