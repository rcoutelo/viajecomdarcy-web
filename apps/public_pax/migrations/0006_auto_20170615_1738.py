# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-15 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_pax', '0005_auto_20170615_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilpublico',
            name='foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='default/pax_public'),
        ),
    ]
