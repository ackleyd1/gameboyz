from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from gameboyz.core.mixins import StaffRequiredMixin

from .models import GameTitle, Game
from .forms import GameTitleUpdateForm, GameUpdateForm

##########################################################
# GameTitle Admin Views (Detail shows list of Games)
##########################################################

class GameTitleListView(StaffRequiredMixin, ListView):
    model = GameTitle
    template_name = 'games/admin/gametitle_list.html'
    context_object_name = 'gametitles'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        gametitles = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            gametitles = gametitles.filter(name__icontains=q)
        return gametitles

class GameTitleCreateView(StaffRequiredMixin, CreateView):
    model = GameTitle
    template_name = 'core/create.html'
    fields = '__all__'

    def get_success_url(self):
      return reverse('gametitles:detail', kwargs={'gametitle_pk': self.object.pk})

class GameTitleDetailView(StaffRequiredMixin, DetailView):
    model = GameTitle
    template_name = 'games/admin/gametitle.html'
    context_object_name = 'gametitle'
    pk_url_kwarg = 'gametitle_pk'

class GameTitleUpdateView(StaffRequiredMixin, UpdateView):
    model = GameTitle
    template_name = 'core/update.html'
    form_class = GameTitleUpdateForm
    pk_url_kwarg = 'gametitle_pk'

    def get_success_url(self):
        return reverse('gametitles:detail', kwargs={'gametitle_pk': self.object.pk})

class GameTitleDeleteView(StaffRequiredMixin, DeleteView):
    model = GameTitle
    template_name = 'core/delete.html'
    success_url = reverse_lazy('gametitles:list')
    pk_url_kwarg = 'gametitle_pk'

##########################################################
# Game Admin Views
##########################################################

class GameCreateView(StaffRequiredMixin, CreateView):
    model = Game
    fields = ['edition', 'baseconsole', 'asin', 'epid', 'image']
    template_name = 'core/create.html'

    def get_success_url(self):
        return reverse('gametitles:games-detail', kwargs={'gametitle_pk': self.object.gametitle.pk, 'game_pk': self.object.pk})

    def form_valid(self, form):
        game = form.save(commit=False)
        game.gametitle = GameTitle.objects.get(pk=self.kwargs.get('gametitle_pk'))
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
        return reverse('gametitles:games-detail', kwargs={'gametitle_pk': self.object.gametitle.pk, 'game_pk': self.object.pk})

class GameDeleteView(StaffRequiredMixin, DeleteView):
    model = Game
    template_name = 'core/delete.html'
    pk_url_kwarg = 'game_pk'

    def get_success_url(self):
        return reverse('gametitles:detail', kwargs={'gametitle_pk': self.object.gametitle.pk})