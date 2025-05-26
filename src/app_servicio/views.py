from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Servicio

class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'create.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('app_servicio:servicio_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nuevo servicio'
        return context
