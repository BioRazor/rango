# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_category_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='like',
            new_name='likes',
        ),
    ]
