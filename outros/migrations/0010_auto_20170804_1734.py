# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 21:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outros', '0009_auto_20170804_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 17, 34, 53, 476699)),
        ),
    ]
