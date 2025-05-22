from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente

# Create your views here.

class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_generica.html"
    context_object_name = "objetos" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Clientes"
        context["encabezados_campos"] = [campo.verbose_name for campo in Cliente._meta.fields] 
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in Cliente._meta.fields]
            for obj in context["objetos"]
        ]
        return context
