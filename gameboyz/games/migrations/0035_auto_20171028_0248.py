# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 02:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0034_auto_20171028_0215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamelisting',
            old_name='uuid',
            new_name='id',
        ),
    ]
