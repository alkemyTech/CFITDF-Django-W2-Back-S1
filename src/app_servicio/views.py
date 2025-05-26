from django.shortcuts import render
from django.views.generic import CreateView, ListView
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

class ServicioListView(ListView):
    model = Servicio
    template_name = "lista_generica.html"
    context_object_name = "objetos" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Servicios"
        context["encabezados_campos"] = [campo.verbose_name for campo in Servicio._meta.fields] 
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in Servicio._meta.fields]
            for obj in context["objetos"]
        ]
        return context