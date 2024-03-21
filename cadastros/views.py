from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from cadastros.models import Estagio, Estudante

# Create your views here.
class EstudanteCreateView(LoginRequiredMixin, CreateView):
    model = Estudante
    fields = "__all__"
    
class EstagioCreateView(LoginRequiredMixin, CreateView):
    model = Estagio
    fields = "__all__"
    
    