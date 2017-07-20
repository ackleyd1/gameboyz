# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('igdb', models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True)),
            ],
        ),
    ]
