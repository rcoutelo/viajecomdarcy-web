# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-05-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursao',
            name='is_internacional',
            field=models.BooleanField(default=False),
        ),
    ]
