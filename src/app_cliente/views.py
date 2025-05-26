from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
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

    def get_success_url(self):
        return reverse_lazy('app_cliente:cliente_update', 
                            kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'cliente'
      
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
        return context
