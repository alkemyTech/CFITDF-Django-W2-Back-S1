from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "lista_generica.html"
    context_object_name = "objetos" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Empleados"
        context["encabezados_campos"] = [campo.verbose_name for campo in Empleado._meta.fields] 
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in Empleado._meta.fields]
            for obj in context["objetos"]
        ]
        return context
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido','legajo']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('app_empleado:empleado_update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'empleado'
        return context
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "borrado.html"
    success_url = reverse_lazy("app_empleado:empleado_lista")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context
