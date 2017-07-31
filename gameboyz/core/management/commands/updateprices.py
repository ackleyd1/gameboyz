from django.core.management.base import BaseCommand, CommandError

from gameboyz.consoles.models import BaseConsole

class Command(BaseCommand):
    help = 'Updates pricing information for games'

    def handle(self, *args, **options):
        