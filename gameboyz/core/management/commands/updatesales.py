import json
import dateutil.parser

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from gameboyz.consoles.models import Console
from gameboyz.games.models import Game

from gameboyz.sales.models import GameSale, ConsoleSale

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

class Command(BaseCommand):
    help = 'Updates ebay prices everyday'

    def handle(self, *args, **options):
        for game in Game.objects.all():
            try:
              api = Connection(appid=settings.EBAY_APP_ID, config_file=None)
              response = api.execute('findCompletedItems', {'keywords': ' '.join(game.slug.split('-')), 'categoryId': '139973'})
              if response.reply.ack == 'Success' and 'item' in response.dict()['searchResult'].keys():
                  for item in response.dict()['searchResult']['item']:
                      if 'productId' in item.keys():
                          if game.epid == item['productId']['value'] and not GameSale.objects.filter(url=item['viewItemURL']).exists() and item['sellingStatus']['sellingState'] == "EndedWithSales" and item['sellingStatus']['convertedCurrentPrice']["_currencyId"] == "USD" and item['country'] == 'US':
                              GameSale.objects.create(
                                  title=item['title'],
                                  game=game,
                                  country=item['country'],
                                  location=item['location'],
                                  url=item['viewItemURL'],
                                  condition=item['condition']['conditionDisplayName'],
                                  price=item['sellingStatus']['convertedCurrentPrice']['value'],
                                  sold=dateutil.parser.parse(item['listingInfo']['endTime'])
                              )
            except ConnectionError as e:
                print(e)
                print(e.response.dict())
                print(game.gametitle.name)
        for console in Console.objects.all():
            try:
              api = Connection(appid=settings.EBAY_APP_ID, config_file=None)
              response = api.execute('findCompletedItems', {'keywords': ' '.join(console.slug.split('-')), 'categoryId': '139971'})
              if response.reply.ack == 'Success' and 'item' in response.dict()['searchResult'].keys():
                  for item in response.dict()['searchResult']['item']:
                      if 'productId' in item.keys():
                          if console.epid == item['productId']['value'] and not ConsoleSale.objects.filter(url=item['viewItemURL']).exists() and item['sellingStatus']['sellingState'] == "EndedWithSales" and item['sellingStatus']['convertedCurrentPrice']["_currencyId"] == "USD" and item['country'] == 'US':
                              ConsoleSale.objects.create(
                                  title=item['title'],
                                  console=console,
                                  country=item['country'],
                                  location=item['location'],
                                  url=item['viewItemURL'],
                                  condition=item['condition']['conditionDisplayName'],
                                  price=item['sellingStatus']['convertedCurrentPrice']['value'],
                                  sold=dateutil.parser.parse(item['listingInfo']['endTime'])
                              )

            except ConnectionError as e:
                print(e)
                print(e.response.dict())
                print(console.baseconsole.name)