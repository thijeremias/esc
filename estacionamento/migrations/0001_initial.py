# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('tel1', models.CharField(max_length=11, verbose_name='Telefone')),
                ('tel2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone 2')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Hora')),
                ('valor_hora_moto', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor Hora Moto')),
            ],
            options={
                'verbose_name_plural': 'Configurações',
                'verbose_name': 'Configuração',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True, verbose_name='Placa')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name_plural': 'Entradas',
                'verbose_name': 'Entrada',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora')),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.Entrada', verbose_name='Placa')),
            ],
            options={
                'verbose_name_plural': 'Saidas',
                'verbose_name': 'Saída',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=7, unique=True, verbose_name='Placa do veículo')),
                ('cor', models.CharField(max_length=10, verbose_name='Cor do veículo')),
                ('mensalista', models.BooleanField(default=True, verbose_name='Mensalista')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Mensalidade')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Marca', verbose_name='Marca')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.Cliente', verbose_name='Proprietário')),
            ],
            options={
                'verbose_name_plural': 'Veículos',
                'verbose_name': 'Veículo',
                'ordering': ['proprietario'],
            },
        ),
    ]
