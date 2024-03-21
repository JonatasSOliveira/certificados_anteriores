from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from cadastros.models import Estagio, Estudante

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    

class EstudanteCreateView(LoginRequiredMixin, CreateView):
    model = Estudante
    fields = "__all__"


class EstagioCreateView(LoginRequiredMixin, CreateView):
    model = Estagio
    fields = "__all__"
    