# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20170719_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basegame',
            name='first_release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
