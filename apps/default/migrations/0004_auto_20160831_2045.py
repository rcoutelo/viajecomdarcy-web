# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_auto_20160831_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]