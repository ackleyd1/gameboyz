# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import gameboyz.games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20170731_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=gameboyz.games.models.image_path_rename),
        ),
    ]