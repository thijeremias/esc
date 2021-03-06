# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_remove_marca_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='valor',
            field=models.FloatField(default=0, verbose_name='Valor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=30, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Marca', verbose_name='Marca'),
        ),
    ]
