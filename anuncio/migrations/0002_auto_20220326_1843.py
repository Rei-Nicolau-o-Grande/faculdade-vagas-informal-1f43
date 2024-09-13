# Generated by Django 3.2.9 on 2022-03-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='descricao_curta',
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='descricao_longa',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='descricao',
            field=models.TextField(default=' ', verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='categorias',
            field=models.CharField(choices=[('Tecnologia', 'Tecnologia'), ('Mercado Financeiro', 'Mercado Financeiro'), ('Finanças e contabilidade', 'Finanças e contabilidade'), ('Vendas e marketing', 'Vendas e marketing'), ('Jurídico', 'Jurídico'), ('Educação', 'Educação')], default=' ', max_length=50, verbose_name='Tipo da Vaga'),
        ),
    ]
