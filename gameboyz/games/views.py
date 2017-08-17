from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from gameboyz.core.mixins import UserMixin

from .models import BaseGame, Game, GameListing
from .forms import BaseGameUpdateForm, GameUpdateForm

class GameListView(UserMixin, ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    paginate_by = 20
    queryset = Game.objects.all().annotate(sale_count=Count('sale')).order_by('-sale_count')

class GameDetailView(UserMixin, DetailView):
    model = Game
    template_name = 'games/game.html'
    context_object_name = 'game'

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'core/update.html'
    form_class = GameUpdateForm

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'core/delete.html'
    success_url = reverse_lazy('games:list')

class BaseGameListView(UserMixin, ListView):
    model = BaseGame
    template_name = 'games/basegame_list.html'
    context_object_name = 'basegames'
    paginate_by = 20
    queryset = BaseGame.objects.all().annotate(sale_count=Count('game__sale')).order_by('-sale_count')

class BaseGameDetailView(UserMixin, DetailView):
    model = BaseGame
    template_name = 'games/basegame.html'
    context_object_name = 'basegame'

class BaseGameUpdateView(UpdateView):
    model = BaseGame
    template_name = 'core/update.html'
    form_class = BaseGameUpdateForm

class BaseGameDeleteView(DeleteView):
    model = BaseGame
    template_name = 'core/delete.html'
    success_url = reverse_lazy('basegame-list')

class GameListingCreateView(CreateView):
    model = GameListing
    template_name = 'core/create.html'
    fields = ["price", "condition"]

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)
        form.instance.game = Game.objects.get(id=self.kwargs.get('pk'))
        return super(GameListingCreateView, self).form_valid(form)