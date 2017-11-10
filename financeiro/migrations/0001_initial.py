# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacionamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('data_pagamento', models.DateField(default=datetime.date(2017, 10, 31), verbose_name='Data de Pagamento')),
            ],
        ),
        migrations.CreateModel(
            name='ContasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')], verbose_name='Mês')),
                ('data_pagamento', models.DateField(default=datetime.date(2017, 10, 31), verbose_name='Data de Pagamento')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.Veiculo', verbose_name='Veiculo')),
            ],
            options={
                'verbose_name_plural': 'Contas a Receber',
                'verbose_name': 'Contas a Receber',
                'ordering': ['data_pagamento'],
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=25, verbose_name='Movimento')),
            ],
            options={
                'verbose_name_plural': 'Movimentos',
                'verbose_name': 'Movimento',
                'ordering': ['descricao'],
            },
        ),
        migrations.AddField(
            model_name='caixa',
            name='movimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Movimento', verbose_name='Movimento'),
        ),
    ]
