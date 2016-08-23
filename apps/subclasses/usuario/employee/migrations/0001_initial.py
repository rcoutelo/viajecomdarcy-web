# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]