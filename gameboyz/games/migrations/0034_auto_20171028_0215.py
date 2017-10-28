# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0033_auto_20171028_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelisting',
            name='condition',
            field=models.CharField(choices=[('new', 'Brand New'), ('Complete In Box', (('cibvgood', 'Very Good'), ('cibgood', 'Good'), ('cibacceptable', 'Acceptable'))), ('Loose', (('loosevgood', 'Very Good'), ('loosegood', 'Good'), ('looseacceptable', 'Acceptable')))], max_length=32),
        ),
    ]
