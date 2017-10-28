from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from gameboyz.core.mixins import StaffRequiredMixin

from .models import BaseGame, Game
from .forms import BaseGameUpdateForm, GameUpdateForm

##########################################################
# BaseGame Admin Views (Detail shows list of Games)
##########################################################

class BaseGameListView(StaffRequiredMixin, ListView):
    model = BaseGame
    template_name = 'games/admin/basegame_list.html'
    context_object_name = 'basegames'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        basegames = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            basegames = basegames.filter(name__icontains=q)
        return basegames

class BaseGameCreateView(StaffRequiredMixin, CreateView):
    model = BaseGame
    template_name = 'core/create.html'
    fields = '__all__'

    def get_success_url(self):
      return reverse('basegames:detail', kwargs={'basegame_pk': self.object.pk})

class BaseGameDetailView(StaffRequiredMixin, DetailView):
    model = BaseGame
    template_name = 'games/admin/basegame.html'
    context_object_name = 'basegame'
    pk_url_kwarg = 'basegame_pk'

class BaseGameUpdateView(StaffRequiredMixin, UpdateView):
    model = BaseGame
    template_name = 'core/update.html'
    form_class = BaseGameUpdateForm
    pk_url_kwarg = 'basegame_pk'

    def get_success_url(self):
        return reverse('basegames:detail', kwargs={'basegame_pk': self.object.pk})

class BaseGameDeleteView(StaffRequiredMixin, DeleteView):
    model = BaseGame
    template_name = 'core/delete.html'
    success_url = reverse_lazy('basegames:list')
    pk_url_kwarg = 'basegame_pk'

##########################################################
# Game Admin Views
##########################################################

class GameCreateView(StaffRequiredMixin, CreateView):
    model = Game
    fields = ['edition', 'baseconsole', 'asin', 'epid', 'image']
    template_name = 'core/create.html'

    def get_success_url(self):
        return reverse('basegames:games-detail', kwargs={'basegame_pk': self.object.basegame.pk, 'game_pk': self.object.pk})

    def form_valid(self, form):
        game = form.save(commit=False)
        game.basegame = BaseGame.objects.get(pk=self.kwargs.get('basegame_pk'))
        self.object = game.save()
        return super().form_valid(form)

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
        return reverse('basegames:games-detail', kwargs={'basegame_pk': self.object.basegame.pk, 'game_pk': self.object.pk})

class GameDeleteView(StaffRequiredMixin, DeleteView):
    model = Game
    template_name = 'core/delete.html'
    pk_url_kwarg = 'game_pk'

    def get_success_url(self):
        return reverse('basegames:detail', kwargs={'basegame_pk': self.object.basegame.pk})