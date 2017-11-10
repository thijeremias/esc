# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0003_auto_20171031_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saida',
            options={'ordering': ['datetime'], 'verbose_name': 'Saída', 'verbose_name_plural': 'Saidas'},
        ),
        migrations.AlterField(
            model_name='entrada',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Carro'), (1, 'Moto')], default=1, verbose_name='Carro ou Moto?'),
        ),
    ]
