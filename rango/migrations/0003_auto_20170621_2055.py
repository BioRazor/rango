# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170621_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='tittle',
            new_name='title',
        ),
    ]
