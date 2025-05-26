from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Empleado

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'create.html'
    fields = ['nombre', 'apellido','legajo']
    success_url = reverse_lazy('app_empleado:empleado_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'registrar empleado'
        return context
