from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, ListView,
    DeleteView, DetailView
)
from django.urls import reverse_lazy
from .models import Empleado


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'create.html'
    fields = ['nombre', 'apellido', 'legajo']
    success_url = reverse_lazy('app_empleado:empleado_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nuevo empleado'
        return context


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "listas/empleado.html"
    context_object_name = "empleados"

    def get_queryset(self):

        show_inactive = self.kwargs.get('show_inactive', False)
        if show_inactive:
            return Empleado.all_objects.filter(activo=False)
        return Empleado.objects.all()


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'legajo', 'activo']
    template_name = 'update.html'

    def get_queryset(self):
        return Empleado.all_objects.all()

    def get_success_url(self):
        return reverse_lazy('app_empleado:empleado_update',
                            kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'empleado'
        context["success_url"] = reverse_lazy('app_empleado:empleado_lista_activos')
        return context


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "borrado.html"
    success_url = reverse_lazy("app_empleado:empleado_lista_activos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'details.html'
    context_object_name = 'objeto'

    def get_queryset(self):
        return Empleado.all_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "empleado"
        context["campos"] = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.model._meta.fields
        ]
        return context
