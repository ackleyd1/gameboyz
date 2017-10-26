from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Avg, Count, Sum, Min, Sum

from gameboyz.core.mixins import StaffRequiredMixin

from gameboyz.games.models import Game
from gameboyz.consoles.models import Console, BaseConsole
from .models import GameSale, ConsoleSale

MONTHS = {
    'January' : 1,
    'February' : 2,
    'March' : 3,
    'April' : 4,
    'May' : 5,
    'June' : 6,
    'July' : 7,
    'August' : 8,
    'September' : 9,
    'October' : 10,
    'November' : 11,
    'December' : 12,
}

class SaleSummaryView(StaffRequiredMixin, TemplateView):
    template_name = 'sales/admin/summary.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['baseconsoles'] = BaseConsole.objects.all()
        context['gamesales'] = GameSale.objects.aggregate(Sum('price'), Avg('price'), Count('price'), Min('sold'), Min('created'))
        context['gamesales']['game__count'] = Game.objects.count()
        context['data'] = []
        for baseconsole in BaseConsole.objects.all():
            context['data'] += [GameSale.objects.filter(game__baseconsole__slug=baseconsole.slug).aggregate(Sum('price'))['price__sum'],]
        context['gamesales']['months'] = sorted([{'name': month, 'total': GameSale.objects.filter(sold__month = MONTHS[month]).aggregate(Sum('price'))['price__sum']} for month in MONTHS], key=lambda x: MONTHS[x['name']])
        return context