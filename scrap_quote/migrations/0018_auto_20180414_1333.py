# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0017_auto_20180413_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='hazardous_mats',
            field=models.ManyToManyField(null=True, to='scrap_quote.HazardousMaterials'),
        ),
    ]
