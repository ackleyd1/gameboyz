from __future__ import absolute_import

from celery import shared_task

import json
import dateutil.parser

from django.conf import settings

from gameboyz.games.models import Game
from gameboyz.sales.models import Sale

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

@shared_task(name='updatesales')
def updatesales():
    for game in Game.objects.all()[:5]:
        try:
            api = Connection(appid=settings.EBAY_APP_ID, config_file=None)
            response = api.execute('findCompletedItems', {'keywords': ' '.join(game.slug.split('-')), 'categoryId': '139973'})
            if response.reply.ack == 'Success' and 'item' in response.dict()['searchResult'].keys():
                for item in response.dict()['searchResult']['item']:
                    if 'productId' in item.keys():
                        if game.epid == item['productId']['value'] and not Sale.objects.filter(url=item['viewItemURL']).exists() and item['sellingStatus']['sellingState'] == "EndedWithSales" and item['sellingStatus']['convertedCurrentPrice']["_currencyId"] == "USD" and item['country'] == 'US':
                            Sale.objects.create(
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
            continue