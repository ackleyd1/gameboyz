# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
