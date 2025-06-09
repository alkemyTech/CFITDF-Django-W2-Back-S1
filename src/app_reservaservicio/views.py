from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView,
    DeleteView, DetailView
)
from django.urls import reverse_lazy
from .models import ReservaServicio


class ReservaServicioCreateView(CreateView):
    model = ReservaServicio
    template_name = 'create.html'
    fields = ['fecha_evento', 'cliente', 'servicio', 'empleado', 'coordinador']
    success_url = reverse_lazy('app_reservaservicio:reserva_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nueva reserva'
        return context


class ReservaServicioListView(ListView):
    model = ReservaServicio
    template_name = "listas/reserva_servicio.html"
    context_object_name = "reservas"

    def get_queryset(self):

        return ReservaServicio.objects.all()


class ReservaServicioUpdateView(UpdateView):
    model = ReservaServicio

    fields = ['fecha_evento', 'cliente', 'servicio', 'empleado', 'coordinador']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('app_reservaservicio:reserva_update',
                            kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'reserva'
        context["success_url"] = reverse_lazy('app_reservaservicio:reserva_lista')
        return context


class ReservaServicioDeleteView(DeleteView):
    model = ReservaServicio
    template_name = "borrado.html"
    success_url = reverse_lazy("app_reservaservicio:reserva_lista")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context


class ReservaServicioDetailView(DetailView):
    model = ReservaServicio
    template_name = 'details.html'
    context_object_name = 'objeto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "reserva"
        context["campos"] = [
            (field.verbose_name, getattr(self.object, field.name))
            for field in self.model._meta.fields
        ]
        return context
