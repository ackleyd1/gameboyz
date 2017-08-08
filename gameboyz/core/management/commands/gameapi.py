import csv, os

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from django.db.utils import IntegrityError

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

            slugs = {18: [], 19: [], 4: [], 21: [], 33: [], 22: [], 24: []}

            for row in read_price_guide:
                console = row[1]
                name = row[2]
                asin = row[12]
                epid = row[13]

                if console in consoles.keys() and name and (epid or asin):
                    console = BaseConsole.objects.get(igdb=consoles[console])
                    slug = slugify(name)

                    if Game.objects.filter(console=console.id, slug=slug).exists():
                        game = Game.objects.filter(console=console.id, slug=slug).first()
                        if game.verified:
                            # dont set it
                            continue
                        else:
                            # set it and add to list of slugs to not set
                            if asin and asin != "none":
                                game.asin = asin 
                            if epid:
                                game.epid = epid
                            game.save()
                            slugs[console.igdb].append(slug)
                    else:
                        words = slug.split('-')
                        qs = Game.objects.filter(console=console.id, verified=False, epid=None, asin=None)

                        if '1' in words:
                            words.append('i')
                        if '2' in words:
                            words.append('ii')
                        if '3' in words:
                            words.append('iii')
                        if '4' in words:
                            words.append('iv')
                        if '5' in words:
                            words.append('v')
                        
                        if 'i' in words:
                            words.append('1')
                        if 'ii' in words:
                            words.append('2')
                        if 'iii' in words:
                            words.append('3')
                        if 'iv' in words:
                            words.append('4')
                        if 'v' in words:
                            words.append('5')

                        qs = qs.filter(basegame__name__icontains=words[0])

                        for slug in slugs[console.igdb]:
                            qs = qs.exclude(slug=slug)
                        
                        for word in words[1:]:
                            if qs.filter(basegame__name__icontains=word).count() == 0:
                                continue
                            else:
                                qs = qs.filter(basegame__name__icontains=word)
                        
                        if qs.count() < 10 and qs.exists():
                            game = qs.first()
                            try:
                                if asin and asin != "none":
                                    game.asin = asin 
                                if epid:
                                    game.epid = epid
                                game.save()
                            except IntegrityError:
                                continue
                                