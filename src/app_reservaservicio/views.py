from django.shortcuts import render
from django.views.generic import CreateView, ListView
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
    