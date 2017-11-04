# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 22:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='ConsoleListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('condition', models.CharField(max_length=32)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Console')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='console',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Platform'),
        ),
    ]