# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-19 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='pacote_desc',
            field=models.TextField(max_length=200),
        ),
    ]
