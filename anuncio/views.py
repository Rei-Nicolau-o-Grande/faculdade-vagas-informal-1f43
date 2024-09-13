from errno import EDEADLK
from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

class ListaAnuncio(ListView):
    model = models.Anuncio
    context_object_name = 'anuncio'
    template_name = 'lista.html'


class DetalheAnuncio(DetailView):
    model = models.Anuncio
    context_object_name = 'anuncio'
    template_name = 'detalhe_anuncio.html'


class Contratante(ListView):
    queryset = models.Anuncio.objects.all().filter(tipo_de_oferta='Contratante')
    context_object_name = 'contratantes'
    template_name = 'contratante.html'
    

class Contratado(ListView):
    queryset = models.Anuncio.objects.all().filter(tipo_de_oferta='Contratado')
    context_object_name = 'contratados'
    template_name = 'contratado.html'


class Categorias(ListView):
    queryset = models.Anuncio.objects.all()
    context_object_name = 'categorias'
    template_name = 'categorias.html'

class FiltroCategorias(ListView):
    queryset = models.Anuncio.objects.filter(categorias__in=['Tecnologia','Mercado Financeiro','Finanças e contabilidade','Vendas e marketing','Jurídico','Educação'])
    context_object_name = 'cate'
    template_name = 'filtro_categorias.html'
