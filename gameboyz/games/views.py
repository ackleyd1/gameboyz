from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from gameboyz.consoles.models import BaseConsole
from .models import Game

class GameView(View):
    template_name = 'games/game.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = {}
        console = BaseConsole.objects.get(slug=kwargs.get("console_slug"))
        context['game'] = Game.objects.filter(console=console, slug=kwargs.get("game_slug")).first()
        return context
        

class GameVerifyView(UpdateView):
    model = Game
    fields = ['asin', 'epid', 'verified']
    template_name_suffix = '_verify_form'
    context_object_name = 'game'
    
    def get_success_url(self):
        return reverse_lazy('console_verify', kwargs={'console_slug': self.kwargs.get('console_slug','')})
        
    def get_object(self):
        console = BaseConsole.objects.get(slug=self.kwargs.get("console_slug"))
        obj = Game.objects.filter(console=console, slug=self.kwargs.get("game_slug")).first()
        return obj

class GameDeleteView(DeleteView):
    model = Game
    context_object_name = 'game'

    def get_success_url(self):
        return reverse_lazy('console_verify', kwargs={'console_slug': self.kwargs.get('console_slug','')})
        
    def get_object(self):
        console = BaseConsole.objects.get(slug=self.kwargs.get("console_slug"))
        obj = Game.objects.filter(console=console, slug=self.kwargs.get("game_slug")).first()
        return obj


