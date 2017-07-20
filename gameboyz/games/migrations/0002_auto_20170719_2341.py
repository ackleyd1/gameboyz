# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='igdb',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='franchise',
            name='igdb',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='igdb',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='igdb',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
