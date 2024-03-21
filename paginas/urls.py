from django.urls import path

# Importe suas views
from .views import IndexView, SobreView, EstagioCreateView, EstudanteCreateView

urlpatterns = [
    # Crie suas urls para as views
    path("", IndexView.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("estagio/cadastro/", EstagioCreateView.as_view(), name="estagio-cadastro"),
    path("estudante/cadastro/", EstudanteCreateView.as_view(), name="estudante-cadastro"),
]
