# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0003_auto_20170804_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 5, 9, 41, 7, 691614)),
        ),
    ]
