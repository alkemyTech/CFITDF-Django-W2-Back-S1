from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, ListView,
    DeleteView, DetailView
)
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
    fields = ['nombre', 'apellido', 'activo']
    template_name = 'update.html'

    def get_queryset(self):
        return Cliente.all_objects.all()

    def get_success_url(self):
        return reverse_lazy('app_cliente:cliente_update',
                            kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'cliente'
        context["success_url"] = reverse_lazy('app_cliente:cliente_lista')
        return context


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_generica.html"
    context_object_name = "objetos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Clientes"
        context["encabezados_campos"] = [
            campo.verbose_name for campo in Cliente._meta.fields]
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in Cliente._meta.fields]
            for obj in context["objetos"]
        ]
        return context


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "borrado.html"
    success_url = reverse_lazy("app_cliente:cliente_lista")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'details.html'
    context_object_name = 'objeto'

    def get_queryset(self):
        return Cliente.all_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "cliente"
        context["campos"] = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.model._meta.fields
        ]
        return context
