from django.shortcuts import render
from django.views.generic.detail import DetailView

from gameboyz.consoles.models import BaseConsole
from gameboyz.games.models import Game

class ConsoleView(DetailView):
    model = BaseConsole
    context_object_name = 'console'
    template_name = 'consoles/console.html'
    slug_url_kwarg = 'console_slug'

    def get_context_data(self, *args, **kwargs):
        context = super(ConsoleView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['games'] = Game.objects.filter(console=instance.id, verified=False)
        return context
