# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 11:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20171101_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data_emissao',
            field=models.DateField(default=datetime.date(2017, 11, 7), verbose_name='Data de emissão'),
        ),
    ]
