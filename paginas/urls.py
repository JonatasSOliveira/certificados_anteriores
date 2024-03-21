from django.urls import path
from django.contrib.auth.views import LoginView

# Importe suas views
from .views import (
    IndexView, 
    SobreView, 
    EstagioCreateView, 
    EstudanteCreateView, 
    EstudanteListView, 
    EstudanteUpdateView,
    EstudanteDeleteView,
    EstagioListView,
    EstagioUpdateView,
    EstagioDeleteView,
)

urlpatterns = [
    # Crie suas urls para as views
    path("", IndexView.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("estudante/cadastro/", EstudanteCreateView.as_view(), name="estudante-cadastro"),
    path("estudante/lista/", EstudanteListView.as_view(), name="estudante-lista"),
    path("estudante/atualizacao/<int:pk>/", EstudanteUpdateView.as_view(),
         name="estudante-atualizacao"),
    path("estudante/exclusao/<int:pk>/", EstudanteDeleteView.as_view(),
         name="estudante-exclusao"),
    path("estagio/cadastro/", EstagioCreateView.as_view(), name="estagio-cadastro"),
    path("estagio/lista/", EstagioListView.as_view(), name="estagio-lista"),
    path("estagio/atualizacao/<int:pk>/", EstagioUpdateView.as_view(),
         name="estagio-atualizacao"),
    path("estagio/exclusao/<int:pk>/", EstagioDeleteView.as_view(),
         name="estagio-exclusao"),
    path('login/', LoginView.as_view(
        template_name='paginas/usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),

]
