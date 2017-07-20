from django.shortcuts import render
from django.views.generic.detail import DetailView

from gameboyz.games.models import BaseGame

class GameView(DetailView):
    model = BaseGame
    context_object_name = 'game'
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'


