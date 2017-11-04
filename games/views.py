import braintree

from django.core.urlresolvers import reverse
from django.views.generic import View, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.db.models import Count
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity
from django.db.models import Q

from core.mixins import UserMixin, StaffRequiredMixin
from consoles.models import Platform

from .models import Game, GameListing, GameListingImage
from .forms import GameUpdateForm, GameListingUpdateForm, BraintreeSaleForm, GameListingCreateForm

from django.conf import settings

if settings.DEBUG:
    braintree.Configuration.configure(
        braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY
    )

class GameListView(StaffRequiredMixin, UserMixin, ListView):
    """Lists games for a particular platform. Restricted to staff for development purposes."""
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    paginate_by = 20
    queryset = Game.objects.all().prefetch_related('gamesale_set').select_related('platform').annotate(gamesale_count=Count('gamesale')).order_by('-gamesale_count')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        games = super().get_queryset(*args, **kwargs)
        games = games.filter(platform__slug=self.kwargs.get('platform_slug'))
        q = self.request.GET.get('q')
        if q:
            games = games.filter(name__unaccent__icontains=q)
        return games

class GameDetailView(UserMixin, DetailView):
    """Reveals the games details and current listings """
    model = Game
    template_name = 'games/game.html'
    context_object_name = 'game'

    def get_object(self):
        queryset = Game.objects.filter(platform__slug=self.kwargs.get('platform_slug'), slug=self.kwargs.get('game_slug'))
        if not queryset.exists():
            raise ObjectDoesNotExist
        if queryset.count() > 1:
            raise MultipleObjectsReturned
        game = queryset.get()
        return game

##########################################################
# GameListing Views
##########################################################

class GameListingCreateView(CreateView):
    model = GameListing
    template_name = 'core/create.html'
    form_class = GameListingCreateForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('images')
        if form.is_valid():
            return self.form_valid(form, images)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, images):
        gamelisting = form.save(commit=False)
        queryset = Game.objects.filter(platform__slug=self.kwargs.get('platform_slug'), slug=self.kwargs.get('game_slug'))
        if not queryset.exists():
            raise ObjectDoesNotExist
        if queryset.count() > 1:
            raise MultipleObjectsReturned
        game = queryset.get()
        gamelisting.game = game
        gamelisting.user = self.request.user
        self.object = gamelisting.save()
        for image in images:
            GameListingImage.objects.create(image=image, gamelisting=gamelisting)
        return super().form_valid(form)

class GameListingDisplayView(UserMixin, DetailView):
    model = GameListing
    template_name = 'games/gamelisting.html'
    context_object_name = 'gamelisting'
    pk_url_kwarg = 'gamelisting_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['client_token'] = braintree.ClientToken.generate()
        context['sale_form'] = BraintreeSaleForm()
        return context

class GameListingSaleView(SingleObjectMixin, FormView):
    model = GameListing
    template_name = 'games/gamelisting.html'
    form_class = BraintreeSaleForm
    pk_url_kwarg = 'gamelisting_id'

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
            gamelisting.delete()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('games-detail', kwargs={'platform_slug': self.kwargs.get('platform_slug'),'game_slug': self.kwargs.get('game_slug')})

class GameListingDetailView(View):
    def get(self, request, *args, **kwargs):
        view = GameListingDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        view = GameListingSaleView.as_view()
        return view(request, *args, **kwargs)

class GameListingUpdateView(UserMixin, UpdateView):
    model = GameListing
    template_name = 'core/update.html'
    form_class = GameListingUpdateForm
    pk_url_kwarg = 'gamelisting_id'

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied

class GameListingDeleteView(UserMixin, DeleteView):
    model = GameListing
    template_name = 'core/delete.html'
    pk_url_kwarg = 'gamelisting_id'

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('games-detail', kwargs={'platform_slug': self.kwargs.get('platform_slug'),'game_slug': self.kwargs.get('game_slug')})