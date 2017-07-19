import requests
import datetime
import json

from django.conf import settings

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

from gameboyz.games.models import Game, Theme, Keyword, Franchise, Collection, EbayListing
from gameboyz.games.serializer import GameSerializer, ThemeSerializer, KeywordSerializer, FranchiseSerializer, CollectionSerializer, EbayListingSerializer

from gameboyz.consoles.models import Platform
from gameboyz.consoles.serializer import PlatformSerializer

r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/platforms/33?fields=id,name,slug,games', headers={
    "X-Mashape-Key": settings.X_MASHAPE_KEY,
    "Accept": "application/json"})

platform = r.json()[0]

games = platform['games']
del platform['games']

platform_serializer = PlatformSerializer(data=platform)

if platform_serializer.is_valid():

    if not Platform.objects.filter(id=platform['id']).exists():
        platform = platform_serializer.save()

    for game in games:
        r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/games/' + str(game) + '?fields=id,name,slug,summary,url,collection,franchise,popularity,total_rating,total_rating_count,first_release_date,release_dates,keywords,themes', headers={
            "X-Mashape-Key": settings.X_MASHAPE_KEY,
            "Accept": "application/json"})

        game = r.json()[0]

        if Game.objects.filter(id=game['id']).exists():
            print(game['name'], " already exists")
        else:
            # assert we have all the info we technically require
            assert('name' in game.keys()), "summary is not in game keys for game %r" % game['name']
            assert('slug' in game.keys()), "slug is not in game keys for game %r" % game['name']
            assert('url' in game.keys()), "url is not in game keys for game %r" % game['name']
            assert('popularity' in game.keys()), "popularity is not in game keys for game %r" % game['name']
            assert('first_release_date' in game.keys()), "first_release_date is not in game keys for game %r" % game['name']
            assert('release_dates' in game.keys()), "release_dates is not in game keys for game %r" % game['name']

            # manage the collection
            if 'collection' in game.keys():
                # get or create the collection if it doesnt exist
                if Collection.objects.filter(id=game['collection']).exists():
                    print('Collection already exists, adding to collection')
                    game['collections'] = []
                    game['collections'].append(str(game['collection']))
                    del game['collection']

                else:
                    print('Collection does not exist, creating and adding to collection')
                    r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/collections/' + str(game['collection']) + '?fields=id,name,slug', headers={
                        "X-Mashape-Key": settings.X_MASHAPE_KEY,
                        "Accept": "application/json"})

                    if len(r.json()) >= 1:
                        collection = r.json()[0]
                        collection_serializer = CollectionSerializer(data=collection)

                        if collection_serializer.is_valid():
                            collection_serializer.save()
                            game['collections'] = []
                            game['collections'].append(str(game['collection']))
                            del game['collection']
                        else:
                            print("collection serializer is not valid")

            if 'franchise' in game.keys():
                if Franchise.objects.filter(id=game['franchise']).exists():
                    print("Franchise object already exists, adding to franchise")
                else:
                    print("Franchise object doesn not exist, creating and adding it")
                    r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/franchises/' + str(game['franchise']) + '?fields=id,name,slug', headers={
                        "X-Mashape-Key": settings.X_MASHAPE_KEY,
                        "Accept": "application/json"})

                    franchise = r.json()[0]
                    franchise_serializer = FranchiseSerializer(data=franchise)

                    if franchise_serializer.is_valid():
                        franchise_serializer.save()
                    else:
                        print("franchise serializer is not valid")


            if 'keywords' in game.keys():
                for keyword_id in game['keywords']:
                    if Keyword.objects.filter(id=keyword_id).exists():
                        print("Keyword object already exists, adding to keywords")
                    else:
                        print("Keyword object does not exists, creating and adding it")
                        r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/keywords/' + str(keyword_id) + '?fields=id,name,slug', headers={
                        "X-Mashape-Key": settings.X_MASHAPE_KEY,
                        "Accept": "application/json"})

                        keyword = r.json()[0]
                        keyword_serializer = KeywordSerializer(data=keyword)

                        if keyword_serializer.is_valid():
                            keyword_serializer.save()
                        else:
                            print("keyword serializer is not valid")


            if 'themes' in game.keys():
                # get or create the themes and set the relation
                for theme_id in game['themes']:
                    if Theme.objects.filter(id=theme_id).exists():
                        print("Theme already exists, adding to themes")
                    else:
                        print("Theme object does not exists, creating and adding it")
                        r = requests.get('https://igdbcom-internet-game-database-v1.p.mashape.com/themes/' + str(theme_id) + '?fields=id,name,slug', headers={
                        "X-Mashape-Key": settings.X_MASHAPE_KEY,
                        "Accept": "application/json"})

                        theme = r.json()[0]
                        theme_serializer = ThemeSerializer(data=theme)

                        if theme_serializer.is_valid():
                            theme_serializer.save()
                        else:
                            print("Theme serializer is not valid")
                        

            # loop through the release_dates and add platforms that exist
            game['platforms'] = []
            for release_date in game['release_dates']:
                if Platform.objects.filter(id=release_date['platform']).exists():
                    game['platforms'].append(release_date['platform'])
                    
            del game['release_dates']

            # serialize the game
            game['first_release_date'] = game['first_release_date'] / 1000

            game_serializer = GameSerializer(data=game)

            if game_serializer.is_valid() and not Game.objects.filter(id=game['id']).exists():
                game = game_serializer.save()

                try:
                    api = Connection(appid=settings.EBAY_APP_ID, config_file=None)

                    response = api.execute('findCompletedItems', {'keywords': game.name, 'categoryId': '139973'})

                    if response.reply.ack == 'Success':
                        assert(type(response.reply.timestamp) == datetime.datetime)
                        # assert(type(response.reply.searchResult.item) == list)

                        # item = response.reply.searchResult.item[0]
                        # assert(type(item.listingInfo.endTime) == datetime.datetime)
                        assert(type(response.dict()) == dict)

                        if 'item' in response.dict()['searchResult'].keys():

                            for item in response.dict()['searchResult']['item']:
                                ebay_listing = dict()
                                ebay_listing['id'] = item['itemId']
                                ebay_listing['title'] = item['title']
                                ebay_listing['game'] = game.id
                                ebay_listing['country'] = item['country']
                                ebay_listing['location'] = item['location']
                                ebay_listing['url'] = item['viewItemURL']
                                ebay_listing['condition'] = item['condition']['conditionDisplayName']
                                ebay_listing['price'] = item['sellingStatus']['convertedCurrentPrice']['value']

                                ebay_listing_serializer = EbayListingSerializer(data=ebay_listing)

                                if ebay_listing_serializer.is_valid() and not EbayListing.objects.filter(id=ebay_listing['id']).exists():
                                    ebay_listing_serializer.save()
                                else:
                                    print("Ebay listing is not valid")
                                    print(ebay_listing_serializer.errors)

                    
                except ConnectionError as e:
                    print(e)
                    print(e.response.dict())
            else:
                print('Game serializer is not valid or game already exists')
                print(game_serializer.errors)
else:
    print("platform serializer is not valid or platform already exists")
    print(platform_serializer.errors)