# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0005_consolelisting'),
        ('sales', '0006_auto_20170817_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsoleSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=16)),
                ('location', models.CharField(max_length=64)),
                ('url', models.URLField(db_index=True, unique=True)),
                ('condition', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('sold', models.DateTimeField()),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Console')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]