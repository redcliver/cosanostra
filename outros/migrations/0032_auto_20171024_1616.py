# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 19:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0031_auto_20171024_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 16, 16, 13, 280155)),
        ),
        migrations.AlterField(
            model_name='comanda_corte',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 16, 16, 13, 393440)),
        ),
    ]
