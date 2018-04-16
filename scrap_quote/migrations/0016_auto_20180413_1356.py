# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0015_auto_20180411_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date_paid',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quote',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quote',
            name='payment_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
