# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-11 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0013_passageiroopcional_id_reserva_passageiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservapassageiro',
            name='passageiro_opcional',
            field=models.ManyToManyField(to='venda.PassageiroOpcional'),
        ),
    ]