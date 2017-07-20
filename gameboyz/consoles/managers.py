import requests

from django.conf import settings
from django.db import models

from gameboyz.games.models import BaseGame

class BaseConsoleManager(models.Manager):
    def api_create(self, id):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/platforms/' + str(id) + '?fields=id,name,games', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        console = r.json()[0]
        console['id'] = int(console['id'])
        self.create(name=console['name'], igdb=console['id'])