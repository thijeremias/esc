# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='des',
            field=models.CharField(default=0, max_length=30, verbose_name='Marca'),
            preserve_default=False,
        ),
    ]
