# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0027_auto_20180415_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('a', 'All Inclusive'), ('d', 'Disposal Only')], max_length=1, null=True),
        ),
    ]
