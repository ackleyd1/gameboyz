from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.db.models import Count, Min, Sum

from consoles.models import Platform, Console
from games.models import Game, GameListing

from .mixins import UserMixin, StaffRequiredMixin
from .forms import CrispyLoginForm, CrispySignupForm

class HomeView(UserMixin, TemplateView):
    """View for the home page. Can search all games in the database."""
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['platforms'] = Platform.objects.all()
        q = self.request.GET.get('q')
        platform = self.request.GET.get('platform')
        if q:
            games = Game.objects.filter(gametitle__name__unaccent__icontains=q)
            if platform and platform != 'all':
                games = games.filter(platform__slug=platform)
            context['games']  = games.select_related('gametitle').select_related('platform').annotate(gamesale_count=Count('gamesale'), min_price=Min('gamelisting__price')).order_by('-gamesale_count')
        return context

class PlatformOverviewView(StaffRequiredMixin, UserMixin, TemplateView):
    """View related to a gaming platform. Restricted to staff for development purposes."""
    template_name = 'core/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['platform'] = Platform.objects.filter(slug=self.kwargs.get('platform_slug')).first()
        context['games'] = Game.objects.filter(platform__slug=self.kwargs.get('platform_slug')).select_related('gametitle').prefetch_related('gamesale_set').select_related('platform').annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')
        context['consoles'] = Console.objects.filter(platform__slug=self.kwargs.get('platform_slug')).select_related('platform').prefetch_related('consolesale_set').annotate(consolesale_count=Count('consolesale')).order_by('-consolesale_count')
        return context

class UserCollectionView(UserMixin, DetailView):
    """View displaying user's collection of games and later, consoles and accessories."""
    model = User
    template_name = 'core/collection.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.get_object()
        listings = GameListing.objects.filter(user=user).select_related('game__gametitle').prefetch_related('game__gamesale_set')
        value = 0
        for listing in listings:
            price = listing.game.get_price()
            if(price):
                value += price
        context['listings'] = listings
        context['collection_value'] = value
        return context
