# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0020_auto_20180414_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boatinwateroptions',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
