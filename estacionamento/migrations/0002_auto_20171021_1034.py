# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True, verbose_name='Placa')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
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
                'verbose_name': 'Saída',
                'verbose_name_plural': 'Saidas',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel1',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel2',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone 2'),
        ),
    ]
