# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_category_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='like',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
