# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_marca_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='des',
        ),
    ]
