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
    template_name = 'listas/cliente.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        show_inactive = self.kwargs.get('show_inactive', False)
        if show_inactive:
            return Cliente.all_objects.filter(activo=False)
        return Cliente.objects.all()


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "borrado.html"
    success_url = reverse_lazy("app_cliente:cliente_lista_activos")

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
