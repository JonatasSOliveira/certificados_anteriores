from django.forms import BaseModelForm
from django.http import HttpResponse
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


class EstudanteCreateView(LoginRequiredMixin, CreateView):
    model = Estudante
    fields = ["nome", "matricula", "data_nascimento", "email"]
    template_name = "paginas/estudante/cadastro.html"
    success_url = reverse_lazy('estudante-lista')


class EstudanteListView(LoginRequiredMixin, ListView):
    model = Estudante
    template_name = "paginas/estudante/lista.html"
    

class EstudanteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudante
    fields = ["nome", "matricula", "data_nascimento", "email"]
    template_name = "paginas/estudante/atualizacao.html"
    success_url = reverse_lazy('estudante-lista')
    
    
class EstudanteDeleteView(DeleteView):
    model = Estudante
    template_name = "paginas/estudante/exclusao.html"
    success_url = reverse_lazy('estudante-lista')


class EstagioCreateView(LoginRequiredMixin, CreateView):
    model = Estagio
    fields = ["estudante", "empresa", "data_inicio", "data_termino"]
    template_name = "paginas/estagio/cadastro.html"
    success_url = reverse_lazy('estagio-lista')

    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.protocolado_por = self.request.user
        return super().form_valid(form)
        
class EstagioListView(LoginRequiredMixin, ListView):
    model = Estagio
    template_name = "paginas/estagio/lista.html"


class EstagioUpdateView(LoginRequiredMixin, UpdateView):
    model = Estagio
    fields = ["estudante", "empresa", "data_inicio", "data_termino"]
    template_name = "paginas/estagio/atualizacao.html"
    success_url = reverse_lazy('estagio-lista')
    


class EstagioDeleteView(LoginRequiredMixin, DeleteView):
    model = Estagio
    template_name = "paginas/estagio/exclusao.html"
    success_url = reverse_lazy('estagio-lista')
