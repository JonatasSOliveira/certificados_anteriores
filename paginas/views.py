from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from cadastros.models import Estagio, Estudante

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"


class EstudanteCreateView(CreateView):
    model = Estudante
    fields = "__all__"
    template_name = "paginas/estudante/cadastro.html"
    success_url = reverse_lazy('estudante-lista')
    
    
class EstudanteListView(ListView):
    model = Estudante
    template_name = "paginas/estudante/lista.html"
    

class EstudanteUpdateView(UpdateView):
    model = Estudante
    fields = "__all__"
    template_name = "paginas/estudante/atualizacao.html"
    success_url = reverse_lazy('estudante-lista')
    
    
class EstudanteDeleteView(DeleteView):
    model = Estudante
    template_name = "paginas/estudante/exclusao.html"
    success_url = reverse_lazy('estudante-lista')


class EstagioCreateView(LoginRequiredMixin, CreateView):
    model = Estagio
    fields = "__all__"
    template_name = "paginas/estagio/cadastro.html"
    

class EstagioListView(ListView):
    model = Estagio
    template_name = "paginas/estagio/lista.html"


class EstagioUpdateView(UpdateView):
    model = Estagio
    fields = "__all__"
    template_name = "paginas/estagio/atualizacao.html"
    success_url = reverse_lazy('estagio-lista')


class EstagioDeleteView(DeleteView):
    model = Estagio
    template_name = "paginas/estagio/exclusao.html"
    success_url = reverse_lazy('estagio-lista')
