# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20170727_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
