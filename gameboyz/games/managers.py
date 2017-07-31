import requests, datetime

from django.conf import settings
from django.db import models

class ThemeManager(models.Manager):
    def api_create(self, id):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/themes/' + str(id) + '?fields=id,name', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        if len(r.json()) >= 1:
            theme = r.json()[0]

            self.create(name=theme['name'], igdb=theme['id'])
        
        else:
            print("Problem grabbing theme %s" % id)

class KeywordManager(models.Manager):
    def api_create(self, id):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/keywords/' + str(id) + '?fields=id,name', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        if len(r.json()) >= 1:
            keyword = r.json()[0]

            self.create(name=keyword['name'], igdb=keyword['id'])
        
        else:
            print("Problem grabbing keyword %s" % id)

class FranchiseManager(models.Manager):
    def api_create(self, id):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/franchises/' + str(id) + '?fields=id,name', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        if len(r.json()) >= 1:
            franchise = r.json()[0]

            self.create(name=franchise['name'], igdb=franchise['id'])
        
        else:
            print("Problem grabbing franchise %s" % id)

class CollectionManager(models.Manager):
    def api_create(self, id):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/collections/' + str(id) + '?fields=id,name', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        if len(r.json()) >= 1:
            collection = r.json()[0]

            self.create(name=collection['name'], igdb=collection['id'])
        
        else:
            print("Problem grabbing collection %s" % id)

class BaseGameManager(models.Manager):
    def api_create(self, id, *args, **kwargs):
        r = requests.get(settings.IGDB_MASHAPE_URL + '/games/' + str(id) + '?fields=id,name,summary,url,collection,franchise,popularity,total_rating,total_rating_count,first_release_date,release_dates,keywords,themes', 
            headers={
                "X-Mashape-Key": settings.X_MASHAPE_KEY,
                "Accept": "application/json"
        })

        game = r.json()[0]

        assert('name' in game.keys()), "summary is not in game keys for game %r" % game['name']
        assert('url' in game.keys()), "url is not in game keys for game %r" % game['name']
        assert('popularity' in game.keys()), "popularity is not in game keys for game %r" % game['name']
        assert('release_dates' in game.keys()), "release_dates is not in game keys for game %r" % game['name']

        # manage the first_release_date

        first_release_date = None

        if 'first_release_date' in game.keys():
            first_release_date = datetime.datetime.fromtimestamp(int(game['first_release_date'])/ 1000)

        # manage the summary

        summary = None

        if 'summary' in game.keys():
            summary = game['summary']

        # manage the total_rating

        total_rating = None

        if 'total_rating' in game.keys():
            total_rating = game['total_rating']

        # manage the total_rating_count

        total_rating_count = None

        if 'total_rating_count' in game.keys():
            total_rating_count = game['total_rating_count']


        from .models import Game, Theme, Keyword, Franchise, Collection

        # manage the franchise

        franchise = None

        if 'franchise' in game.keys():
            if not Franchise.objects.filter(igdb=game['franchise']).exists():
                Franchise.objects.api_create(game['franchise'])
                print("%s franchise model created." % Franchise.objects.get(igdb=game['franchise']).name)
            else:
                print("%s franchise model already exists." % Franchise.objects.get(igdb=game['franchise']).name)
            franchise = Franchise.objects.get(igdb=game['franchise'])

        # manage the collection
        
        collections = []

        if 'collection' in game.keys():
            if not Collection.objects.filter(igdb=game['collection']).exists():
                Collection.objects.api_create(game['collection'])
            if Collection.objects.filter(igdb=game['collection']).exists():
                collections.append(game['collection'])

        # manage the keywords

        keywords = []

        if 'keywords' in game.keys():
            for game_keyword_id in game['keywords']:
                if not Keyword.objects.filter(igdb=game_keyword_id).exists():
                    Keyword.objects.api_create(game_keyword_id)
                keywords.append(game_keyword_id)

        # manage the themes
        
        themes = []

        if 'themes' in game.keys():
            for theme_id in game['themes']:
                if not Theme.objects.filter(igdb=theme_id).exists():
                    Theme.objects.api_create(theme_id)
                themes.append(theme_id)

        consoles = []

        from gameboyz.consoles.models import BaseConsole

        for release_date in game['release_dates']:
            if BaseConsole.objects.filter(igdb=release_date['platform']).exists(): 
                consoles.append(release_date['platform'])            

        game = self.create(
            name=game['name'],
            url=game['url'],
            first_release_date=first_release_date,
            popularity=game['popularity'],
            summary=summary,
            total_rating=total_rating,
            total_rating_count=total_rating_count,
            franchise=franchise,
            igdb=id,
        )

        for igdb_collection_id in collections:
            game.collections.add(Collection.objects.get(igdb=igdb_collection_id))

        for igdb_collection_id in keywords:
            game.keywords.add(Keyword.objects.get(igdb=igdb_collection_id))

        for igdb_collection_id in themes:
            game.themes.add(Theme.objects.get(igdb=igdb_collection_id))

        for igdb_collection_id in consoles:
            game.consoles.add(BaseConsole.objects.get(igdb=igdb_collection_id))

        for console in game.consoles.all():
            Game.objects.api_create(game, console)
        
class GameManager(models.Manager):
    def api_create(self, basegame, console):
        print(basegame)
        print(console)
        self.create(basegame=basegame, console=console)