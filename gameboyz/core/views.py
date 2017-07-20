from django.shortcuts import render
from django.views.generic.list import ListView

from gameboyz.consoles.models import BaseConsole

class HomeView(ListView):
    model = BaseConsole
    context_object_name = 'consoles'
    template_name = 'core/home.html'