from django.shortcuts import render
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Create your views here.
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "borrado.html"
    success_url = reverse_lazy("app_cliente:cliente_lista")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success_url"] = self.success_url
        return context

