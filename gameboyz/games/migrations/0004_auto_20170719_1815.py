# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20170719_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='collections',
            field=models.ManyToManyField(blank=True, to='games.Collection'),
        ),
        migrations.AlterField(
            model_name='game',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='games.Keyword'),
        ),
        migrations.AlterField(
            model_name='game',
            name='themes',
            field=models.ManyToManyField(blank=True, to='games.Theme'),
        ),
    ]
