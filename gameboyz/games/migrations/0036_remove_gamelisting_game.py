# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0035_auto_20171028_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamelisting',
            name='game',
        ),
    ]