import requests

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from gameboyz.games.models import BaseGame

class Command(BaseCommand):
    help = 'Loads the games in the database'

    def handle(self, *args, **options):
        for console in settings.CONSOLES.keys():
            console_id = settings.CONSOLES[console]
            
            r = requests.get(settings.IGDB_MASHAPE_URL + '/platforms/' + str(console_id) + '?fields=games', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
            })

            games = r.json()[0]['games']

            print(games[:5])

            for game_id in games[:5]:
                if not BaseGame.objects.filter(igdb=game_id).exists():
                    BaseGame.objects.api_create(game_id)
                    print("%s game model created." % BaseGame.objects.get(igdb=game_id).name)
                else:
                    print("%s game model already exists." % BaseGame.objects.get(igdb=game_id).name)