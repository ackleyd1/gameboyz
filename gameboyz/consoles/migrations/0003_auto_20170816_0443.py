# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0002_remove_baseconsole_igdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=128)),
                ('edition', models.CharField(default='Original', max_length=32)),
                ('asin', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('epid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='baseconsole',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseconsole',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='baseconsole',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='console',
            name='baseconsole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.BaseConsole'),
        ),
    ]
