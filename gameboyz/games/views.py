import braintree

from django.forms import ValidationError
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import View, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.conf import settings

from gameboyz.core.mixins import UserMixin

from .models import BaseGame, Game, GameListing
from .forms import BaseGameUpdateForm, GameUpdateForm, BraintreeSaleForm

if settings.DEBUG:
    braintree.Configuration.configure(braintree.Environment.Sandbox,
                                    merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                    public_key=settings.BRAINTREE_PUBLIC_KEY,
                                    private_key=settings.BRAINTREE_PRIVATE_KEY)

class GameListView(UserMixin, ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    paginate_by = 20
    queryset = Game.objects.all().annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        games = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            games = games.filter(basegame__name__icontains=q)
        return games

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
    queryset = BaseGame.objects.all().annotate(gamesale_count=Count('game__gamesale')).order_by('-gamesale_count')

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
        return super().form_valid(form)

class GameListingDisplayView(DetailView):
    model = GameListing
    template_name = 'games/gamelisting.html'
    context_object_name = 'gamelisting'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['client_token'] = braintree.ClientToken.generate()
        context['sale_form'] = BraintreeSaleForm()
        return context

class GameListingSaleView(SingleObjectMixin, FormView):
    template_name = 'games/gamelisting.html'
    form_class = BraintreeSaleForm
    success_url = reverse_lazy('games:list')
    pk_url_kwarg = 'id'
    model = GameListing

    def form_valid(self, form):
        nonce = form.cleaned_data['payment_method_nonce']
        gamelisting = self.get_object()
        result = braintree.Transaction.sale({
            "amount": gamelisting.price,
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True
            }
        })

        if result.is_success or result.transaction:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        gamelisting = self.get_object()
        return reverse('games:detail', kwargs={'pk': gamelisting.game.id})

class GameListingDetailView(View):
    def get(self, request, *args, **kwargs):
        view = GameListingDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = GameListingSaleView.as_view()
        return view(request, *args, **kwargs)