# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 17:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170801_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 1, 13, 35, 28, 134763)),
        ),
    ]
