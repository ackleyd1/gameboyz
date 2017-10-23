from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

from gameboyz.consoles.models import BaseConsole, Console
from gameboyz.games.models import Game, GameListing

from .mixins import UserMixin

class HomeView(UserMixin, TemplateView):
    """HomeView for the website."""
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['baseconsoles'] = BaseConsole.objects.all()
        return context

class BaseConsoleOverviewView(UserMixin, TemplateView):
    """
    Overview for a gaming platform
    **Template:**
    :template:`core/overview.html`
    """
    template_name = 'core/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['games'] = Game.objects.all()[:20]
        context['consoles'] = Console.objects.all()
        return context

class UserCollectionView(UserMixin, DetailView):
    """
    UserCollectionView to view users listed games, consoles, and accessories
    **Template**
    :template:'core/collection.html'
    """
    model = User
    template_name = 'core/collection.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

