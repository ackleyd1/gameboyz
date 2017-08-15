from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from gameboyz.core.views import NameSearchMixin, UserMixin

from .models import Game
from .forms import GameUpdateForm

# class GameListView(UserMixin, NameSearchMixin, ListView):
#     model = Game
#     template_name = 'games/game_list.html'
#     context_object_name = 'games'

#     def get_queryset(self, *args, **kwargs):
#         queryset = super(GameListView, self).get_queryset(*args, **kwargs)
#         queryset = queryset.annotate(sale_count=Count('sale')).order_by('-sale_count')
#         return queryset

def game_list(request):
    games = Game.objects.all().annotate(sale_count=Count('sale')).order_by('-sale_count')
    paginator = Paginator(games, 20)

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        games = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        games = paginator.page(paginator.num_pages)

    return render(request, 'games/game_list.html', {'games': games})

class GameDetailView(UserMixin, DetailView):
    model = Game
    template_name = 'games/game.html'
    context_object_name = 'game'

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'games/game_update.html'
    form_class = GameUpdateForm
    
    def get_success_url(self, *args, **kwargs):
        game = self.get_object(*args, **kwargs)
        return game.get_absolute_url()

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'games/game_delete.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse('games:list')