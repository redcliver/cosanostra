# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 19:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0025_auto_20170812_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 15, 40, 10, 331183)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 15, 40, 10, 335186)),
        ),
    ]
