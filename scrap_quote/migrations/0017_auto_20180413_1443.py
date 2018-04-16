# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 14:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrap_quote', '0016_auto_20180413_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteLogStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=150)),
                ('is_disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='quoteimages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='additional_info',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='engine_cylinders',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='engine_hours',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quotelog',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_log', to='scrap_quote.Quote'),
        ),
        migrations.AddField(
            model_name='quotelog',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scrap_quote.QuoteLogStatus'),
        ),
        migrations.AddField(
            model_name='quotelog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_log', to=settings.AUTH_USER_MODEL),
        ),
    ]
