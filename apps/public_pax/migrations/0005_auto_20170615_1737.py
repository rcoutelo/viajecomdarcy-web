# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-15 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_pax', '0004_perfilpublico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilpublico',
            name='cod_r1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfilpublico',
            name='cod_r2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfilpublico',
            name='cod_r3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]