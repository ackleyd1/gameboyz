# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0003_auto_20170816_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='console',
            name='name',
            field=models.CharField(default='Default', max_length=128),
            preserve_default=False,
        ),
    ]