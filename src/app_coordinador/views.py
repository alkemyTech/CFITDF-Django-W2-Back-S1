from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView,
    DeleteView, DetailView
)
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
    template_name = "listas/coordinador.html"  
    context_object_name = "coordinadores"  

    def get_queryset(self):
        
        show_inactive = self.kwargs.get('show_inactive', False)
        if show_inactive:
            return Coordinador.all_objects.filter(activo=False)
        return Coordinador.objects.all() 


class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    fields = ['nombre', 'apellido', 'numero_documento', 'activo']
    template_name = 'update.html'

    def get_queryset(self):
        return Coordinador.all_objects.all()

    def get_success_url(self):
        return reverse_lazy('app_coordinador:coordinador_update',
                            kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'coordinador'
        context["success_url"] = reverse_lazy('app_coordinador:coordinador_lista_activos')
        return context


class CoordinadorDeleteView(DeleteView):
    model = Coordinador
    template_name = "borrado.html"
    success_url = reverse_lazy("app_coordinador:coordinador_lista_activos")  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context

class CoordinadorDetailView(DetailView):
    model = Coordinador
    template_name = 'details.html'
    context_object_name = 'objeto'

    def get_queryset(self):
        return Coordinador.all_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "coordinador"
        context["campos"] = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.model._meta.fields
        ]
        return context