from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'create.html'
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('app_cliente:cliente_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nuevo cliente'
        return context
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido']
    template_name = 'update.html'
    success_url = reverse_lazy('app_cliente:cliente_update') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'cliente'
        return context
