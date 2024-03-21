from django.contrib import admin

# Importe duas classes
from .models import Cidade, Estudante, Estagio

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Estudante)
admin.site.register(Estagio)
