# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
