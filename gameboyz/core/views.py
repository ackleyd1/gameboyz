from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.db.models import Count

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
        context['baseconsole'] = BaseConsole.objects.filter(slug=self.kwargs.get('baseconsole_slug')).first()
        context['games'] = Game.objects.filter(baseconsole__slug=self.kwargs.get('baseconsole_slug')).select_related('basegame').prefetch_related('gamesale_set').select_related('baseconsole').annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')
        context['consoles'] = Console.objects.filter(baseconsole__slug=self.kwargs.get('baseconsole_slug')).select_related('baseconsole').prefetch_related('consolesale_set').annotate(consolesale_count=Count('consolesale')).order_by('-consolesale_count')
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

