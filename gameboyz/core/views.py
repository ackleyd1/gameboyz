from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.db.models import Count

from gameboyz.consoles.models import BaseConsole, Console
from gameboyz.games.models import Game, GameListing

from .mixins import UserMixin, StaffRequiredMixin
from .forms import CrispyLoginForm, CrispySignupForm

class HomeView(UserMixin, TemplateView):
    """View for the home page. Can search all games in the database."""
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['baseconsoles'] = BaseConsole.objects.all()
        q = self.request.GET.get('q')
        platform = self.request.GET.get('platform')
        if q:
            games = Game.objects.filter(basegame__name__unaccent__icontains=q)
            if platform and platform != 'all':
                games = games.filter(baseconsole__slug=platform)
            context['games']  = games.select_related('basegame').prefetch_related('gamesale_set').select_related('baseconsole').annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')
        return context

class BaseConsoleOverviewView(StaffRequiredMixin, UserMixin, TemplateView):
    """View related to a gaming platform. Restricted to staff for development purposes."""
    template_name = 'core/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['baseconsole'] = BaseConsole.objects.filter(slug=self.kwargs.get('baseconsole_slug')).first()
        context['games'] = Game.objects.filter(baseconsole__slug=self.kwargs.get('baseconsole_slug')).select_related('basegame').prefetch_related('gamesale_set').select_related('baseconsole').annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')
        context['consoles'] = Console.objects.filter(baseconsole__slug=self.kwargs.get('baseconsole_slug')).select_related('baseconsole').prefetch_related('consolesale_set').annotate(consolesale_count=Count('consolesale')).order_by('-consolesale_count')
        return context

class UserCollectionView(UserMixin, DetailView):
    """View displaying user's collection of games and later, consoles and accessories."""
    model = User
    template_name = 'core/collection.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
