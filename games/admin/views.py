from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import StaffRequiredMixin
from games.models import Game
from games.forms import GameUpdateForm

class GameListView(StaffRequiredMixin, ListView):
    model = Game
    template_name = 'games/admin/game_list.html'
    context_object_name = 'games'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        games = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            games = games.filter(name__unaccent__icontains=q)
        return games

class GameCreateView(StaffRequiredMixin, CreateView):
    model = Game
    fields = ['edition', 'platform', 'asin', 'epid', 'image']
    template_name = 'core/create.html'

    def get_success_url(self):
        return reverse('games-admin:games-detail', kwargs={'game_pk': self.object.pk})

class GameDetailView(StaffRequiredMixin, DetailView):
    model = Game
    template_name = 'games/admin/game.html'
    context_object_name = 'game'
    pk_url_kwarg = 'game_pk'

class GameUpdateView(StaffRequiredMixin, UpdateView):
    model = Game
    template_name = 'core/update.html'
    form_class = GameUpdateForm
    pk_url_kwarg = 'game_pk'

    def get_success_url(self):
        return reverse('games-admin:games-detail', kwargs={'game_pk': self.object.pk})

class GameDeleteView(StaffRequiredMixin, DeleteView):
    model = Game
    template_name = 'core/delete.html'
    pk_url_kwarg = 'game_pk'
    success_url = reverse_lazy('games-admin:games-list')
