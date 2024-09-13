from django.contrib import admin

from . import models

class Anuncio_admin(admin.ModelAdmin):
    list_display = [
    'tipo_de_oferta',
    'vaga',
    'categorias',
    'data_anuncio',]

admin.site.register(models.Anuncio, Anuncio_admin)