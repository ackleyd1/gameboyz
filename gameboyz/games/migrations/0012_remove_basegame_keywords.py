# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_auto_20170808_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basegame',
            name='keywords',
        ),
    ]