# Generated by Django 3.2.9 on 2022-03-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_oferta', models.CharField(choices=[('Contratante', 'Contratante'), ('Contratado', 'Contratado')], max_length=15, verbose_name='Oferta')),
                ('vaga', models.CharField(max_length=100, verbose_name='Vagas')),
                ('categorias', models.CharField(choices=[(' ', ' '), ('Tecnologia', 'Tecnologia'), ('Mercado Financeiro', 'Mercado Financeiro'), ('Finanças e contabilidade', 'Finanças e contabilidade'), ('Vendas e marketing', 'Vendas e marketing'), ('Jurídico', 'Jurídico'), ('Educação', 'Educação')], default=' ', max_length=50, verbose_name='Tipo da Vaga')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('data_anuncio', models.DateTimeField(auto_now_add=True, verbose_name='Data do anúncio')),
                ('descricao_curta', models.TextField(max_length=30, verbose_name='Descrição curta')),
                ('descricao_longa', models.TextField(verbose_name='Descrição longa')),
            ],
            options={
                'verbose_name': 'Anúncios',
                'verbose_name_plural': 'Anúncios',
            },
        ),
    ]
