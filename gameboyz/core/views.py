from django.shortcuts import render
from django.views.generic.list import ListView

from gameboyz.consoles.models import BaseConsole

class HomeView(ListView):
    model = BaseConsole
    context_object_name = 'consoles'
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['consoles'] = BaseConsole.objects.all()
        return context

class VerifyView(ListView):
    model = BaseConsole
    context_object_name = 'consoles'
    template_name = 'core/verify.html'