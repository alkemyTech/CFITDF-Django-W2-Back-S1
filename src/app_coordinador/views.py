from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Coordinador

class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'create.html'
    fields = ['nombre', 'apellido', 'numero_documento']
    success_url = reverse_lazy('app_coordinador:coordinador_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nuevo coordinador'
        return context