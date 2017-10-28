# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 13:48
from __future__ import unicode_literals

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    GameListing = apps.get_model('games', 'GameListing')
    for game in GameListing.objects.all():
        game.uuid = uuid.uuid4()
        game.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('games', '0025_gamelisting_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
