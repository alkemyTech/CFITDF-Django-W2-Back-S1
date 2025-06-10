from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView,
    DeleteView, DetailView
)
from django.urls import reverse_lazy, reverse
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
    template_name = "listas/servicio.html"
    context_object_name = "servicios"

    def get_queryset(self):
        show_inactive = self.kwargs.get('show_inactive', False)
        if show_inactive:
            return Servicio.all_objects.filter(activo=False)
        return Servicio.objects.all()


class ServicioUpdateView(UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio', 'activo']
    template_name = 'update.html'

    def get_queryset(self):
        return Servicio.all_objects.all()

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        default_url = reverse('app_servicio:servicio_lista_activos')

        if next_url:
            return next_url
        else:
            return default_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'servicio'
        return context


class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = "borrado.html"
    success_url = reverse_lazy("app_servicio:servicio_lista_activos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'details.html'
    context_object_name = 'objeto'

    def get_queryset(self):
        return Servicio.all_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "servicio"
        context["campos"] = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.model._meta.fields
        ]
        return context