# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caixa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], max_length=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
