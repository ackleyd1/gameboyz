# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='base_game',
            new_name='basegame',
        ),
    ]