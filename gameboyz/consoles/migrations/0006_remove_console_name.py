# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0005_consolelisting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='console',
            name='name',
        ),
    ]