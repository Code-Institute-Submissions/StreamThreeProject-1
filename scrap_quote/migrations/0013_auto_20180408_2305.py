# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0012_auto_20180408_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapatlocation',
            name='scrap_at_location',
            field=models.CharField(max_length=40),
        ),
    ]