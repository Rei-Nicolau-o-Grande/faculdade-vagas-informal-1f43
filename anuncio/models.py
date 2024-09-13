from django.db import models

from django.utils.text import slugify

import string
import random

def aleatorio(): # Gerando uma função que gera letras e numeros até 30 caracteres
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

Tipos_de_vagas = [
        ('Tecnologia','Tecnologia'),
        ('Mercado Financeiro','Mercado Financeiro'),
        ('Finanças e contabilidade','Finanças e contabilidade'),
        ('Vendas e marketing','Vendas e marketing'),
        ('Jurídico','Jurídico'),
        ('Educação','Educação'),
]
oferta = [
    ('Contratante', 'Contratante'),
    ('Contratado','Contratado'),
]
class Anuncio(models.Model):
    tipo_de_oferta = models.CharField('Oferta',max_length=15, choices=oferta)
    vaga = models.CharField('Vagas', max_length=100)
    categorias = models.CharField('Tipo da Vaga', max_length=50, choices=Tipos_de_vagas, default=' ')
    slug = models.SlugField('Slug', max_length=300, unique=True, blank=True, null=True)
    data_anuncio = models.DateTimeField('Data do anúncio', auto_now_add=True)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Anúncios'
        verbose_name_plural = 'Anúncios'

    def __str__(self):
        return f'{self.tipo_de_oferta} {self.vaga} {self.categorias} {self.data_anuncio}'

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.vaga + '-' + self.categorias + '-' + aleatorio()) # concatenando a função com o slug
            self.slug = slug

        super().save(*args, **kwargs)
