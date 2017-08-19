from django.db import models

from gameboyz.core.models import TimeStampedModel
from gameboyz.consoles.models import Console
from gameboyz.games.models import Game

class GameSale(models.Model):
    title = models.CharField(max_length=256)
    game = models.ForeignKey(Game)
    country = models.CharField(max_length=16)
    location = models.CharField(max_length=64)
    url = models.URLField(unique=True, db_index=True)
    condition = models.CharField(max_length=32)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    sold = models.DateTimeField()

    def __str__(self):
        return self.title

class ConsoleSale(TimeStampedModel):
    title = models.CharField(max_length=256)
    console = models.ForeignKey(Console)
    country = models.CharField(max_length=16)
    location = models.CharField(max_length=64)
    url = models.URLField(unique=True, db_index=True)
    condition = models.CharField(max_length=32)
    price = models.FloatField()
    sold = models.DateTimeField()

    def __str__(self):
        return self.title
