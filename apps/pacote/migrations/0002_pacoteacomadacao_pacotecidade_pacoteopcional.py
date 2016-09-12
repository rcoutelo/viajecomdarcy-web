# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursao', '0003_opcional'),
        ('acomodacao', '0001_initial'),
        ('moeda', '0002_auto_20160829_1413'),
        ('pacote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacoteAcomadacao',
            fields=[
                ('id_pacote_acomodacao', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_acomodacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acomadacao_name', to='acomodacao.Acomodacao')),
                ('id_moeda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacote_acomodacao_moeda_name', to='moeda.Moeda')),
                ('id_pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacote_acomodacao_name', to='pacote.Pacote')),
            ],
        ),
        migrations.CreateModel(
            name='PacoteCidade',
            fields=[
                ('id_pacote_cidade', models.AutoField(primary_key=True, serialize=False)),
                ('qtd_dias', models.IntegerField()),
                ('ordem', models.IntegerField()),
                ('id_cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidade_name', to='excursao.Cidade')),
                ('id_pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacote_cidade_name', to='pacote.Pacote')),
            ],
        ),
        migrations.CreateModel(
            name='PacoteOpcional',
            fields=[
                ('id_pacote_opcional', models.AutoField(primary_key=True, serialize=False)),
                ('id_opcional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcional_name', to='excursao.Opcional')),
                ('id_pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacote_name', to='pacote.Pacote')),
            ],
        ),
    ]