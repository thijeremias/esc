# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 17:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_auto_20171010_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='criacao',
            field=models.DateTimeField(default=datetime.date(2017, 10, 11), verbose_name='Criação'),
        ),
    ]