# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passageiro', '0002_auto_20170505_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passageiro',
            name='matricula',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]