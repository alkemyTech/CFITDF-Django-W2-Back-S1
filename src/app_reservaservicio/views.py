from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ReservaServicio

class ReservaServicioCreateView(CreateView):
    model = ReservaServicio
    template_name = 'create.html'
    fields = ['fecha_evento','cliente','servicio','empleado','coordinador']
    success_url = reverse_lazy('app_reservaservicio:reserva_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'nueva reserva'
        return context


class ReservaServicioListView(ListView):
    model = ReservaServicio
    template_name = "lista_generica.html"
    context_object_name = "objetos" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Reservas"
        context["encabezados_campos"] = [campo.verbose_name for campo in ReservaServicio._meta.fields] 
        context["valores_campos"] = [
            [getattr(obj, campo.name) for campo in ReservaServicio._meta.fields]
            for obj in context["objetos"]
        ]
        return context


class ReservaServicioUpdateView(UpdateView):
    model = ReservaServicio
    fields = ['fecha_evento','cliente','servicio','empleado','coordinador']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('app_reservaservicio:reserva_update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'reserva'
        return context


class ReservaServicioDeleteView(DeleteView):
    model = ReservaServicio
    template_name = "borrado.html"
    success_url = reverse_lazy("app_reservaservicio:reserva_lista")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context
