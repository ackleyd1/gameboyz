# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_remove_basegame_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='basegame',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='games.Keyword'),
        ),
        migrations.AlterField(
            model_name='basegame',
            name='franchise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.Franchise'),
        ),
    ]