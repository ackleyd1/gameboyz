from django.db import models

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