from django.shortcuts import render
from django.views.generic import CreateView
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
