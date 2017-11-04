from __future__ import absolute_import
import json
import dateutil.parser

from django.conf import settings

from games.models import Game
from sales.models import GameSale

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute=0, hour=0)),
    name="updatesales",
)
def updatesales():
    """Celery task that loops through our games and gathers pricing info"""
    count = 0
    for game in Game.objects.all():
        try:
            api = Connection(appid=settings.EBAY_APP_ID, config_file=None)
            response = api.execute('findCompletedItems', {'keywords': ' '.join(game.slug.split('-')), 'categoryId': '139973'})
            if response.reply.ack == 'Success' and 'item' in response.dict()['searchResult'].keys():
                for item in response.dict()['searchResult']['item']:
                    if 'productId' in item.keys():
                        url = item['viewItemURL']
                        if game.epid == item['productId']['value'] and not GameSale.objects.filter(url=url).exists() and item['sellingStatus']['sellingState'] == "EndedWithSales" and item['sellingStatus']['convertedCurrentPrice']["_currencyId"] == "USD" and item['country'] == 'US':
                            GameSale.objects.create(
                                title=item['title'],
                                game=game,
                                country=item['country'],
                                location=item['location'],
                                url=url,
                                condition=item['condition']['conditionDisplayName'],
                                price=item['sellingStatus']['convertedCurrentPrice']['value'],
                                sold=dateutil.parser.parse(item['listingInfo']['endTime'])
                            )
                            count += 1
        except ConnectionError as e:
            continue
    logger.info("Games Sales tracked: %s" % count)