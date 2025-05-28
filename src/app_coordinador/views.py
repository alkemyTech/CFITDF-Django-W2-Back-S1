from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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


class CoordinadorListView(ListView):
    model = Coordinador
    template_name = "lista_generica.html"
    context_object_name = "objetos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Clientes"
        context["encabezados_campos"] = [
            campo.verbose_name for campo in Coordinador._meta.fields]
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in Coordinador._meta.fields]
            for obj in context["objetos"]
        ]
        return context


class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    fields = ['nombre', 'apellido', 'numero_documento']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('app_coordinador:coordinador_update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'coordinador'
        return context


class CoordinadorDeleteView(DeleteView):
    model = Coordinador
    template_name = "borrado.html"
    success_url = reverse_lazy("app_coordinador:coordinador_lista")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context
