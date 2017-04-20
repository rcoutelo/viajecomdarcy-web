# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=20, null=True)),
                ('nome', models.CharField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoa.Pessoa')),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('rg', models.CharField(blank=True, max_length=12, null=True)),
                ('orgaoemissor', models.CharField(blank=True, max_length=45, null=True)),
            ],
            bases=('pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoa.Pessoa')),
                ('razao_social', models.CharField(blank=True, max_length=400, null=True)),
            ],
            bases=('pessoa.pessoa',),
        ),
    ]