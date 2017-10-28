from django.db import models

from core.models import TimeStampedModel
from consoles.models import Console
from games.models import Game

class Sale(TimeStampedModel):
    title = models.CharField(max_length=256)
    country = models.CharField(max_length=16)
    location = models.CharField(max_length=64)
    url = models.URLField(unique=True, db_index=True)
    condition = models.CharField(max_length=32)
    price = models.FloatField()
    sold = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class GameSale(Sale):
    game = models.ForeignKey(Game)

class ConsoleSale(Sale):
    console = models.ForeignKey(Console)
