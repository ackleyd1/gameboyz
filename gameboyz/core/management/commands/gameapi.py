import csv, os

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from gameboyz.games.models import Game
from gameboyz.consoles.models import BaseConsole

class Command(BaseCommand):
    help = 'gets epid or asin'

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
                    console = BaseConsole.objects.get(igdb=consoles[console])
                    slug = slugify(name)

                    qs = Game.objects.filter(console=console.id, slug=slug)

                    if qs.exists():
                        game = qs.first()
                        if asin and not game.asin and asin != "none":
                            game.asin = asin 
                        if epid and not game.epid:
                            game.epid = epid
                        game.save()
                    else:
                        print("Could not find model for game %s" % name)