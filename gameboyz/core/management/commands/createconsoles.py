from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from gameboyz.consoles.models import BaseConsole

class Command(BaseCommand):
    help = 'Loads the consoles in the database'

    def handle(self, *args, **options):
        for console in settings.CONSOLES.keys():
            console_id = settings.CONSOLES[console]
            if not BaseConsole.objects.filter(igdb=console_id).exists():
                BaseConsole.objects.api_create(console_id)
                self.stdout.write(self.style.SUCCESS('%s console model created' % console))
            else:
                self.stdout.write(self.style.SUCCESS('%s console model already exists' % console))
                
                