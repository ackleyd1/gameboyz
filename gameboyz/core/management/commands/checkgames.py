import csv, os

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from django.db.utils import IntegrityError

from gameboyz.games.models import Game
from gameboyz.consoles.models import BaseConsole

class Command(BaseCommand):
    help = 'checks the game exists'

    def handle(self, *args, **options):
        price_guide_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'price_guide.csv')

        consoles = {
            'NES': 18,
            'Super Nintendo': 19,
            'Nintendo 64': 4,
            'Gamecube': 21,
            'GameBoy': 33,
            'GameBoy Color': 22,
            'GameBoy Advance': 24,
        }

        with open(price_guide_path) as price_guide_file:
            read_price_guide = csv.reader(price_guide_file, delimiter=',')

            for row in read_price_guide:
                console = row[1]
                name = row[2]
                asin = row[12]
                epid = row[13]

                if console in consoles.keys() and name and (epid or asin):
                    pass
