from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'app_cliente/cliente_form.html'
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('app_cliente:cliente_create')
