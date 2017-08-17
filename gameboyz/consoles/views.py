from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gameboyz.core.mixins import UserMixin

from .models import BaseConsole, Console
from .forms import BaseConsoleUpdateForm, ConsoleUpdateForm

class ConsoleListView(UserMixin, ListView):
    model = Console
    template_name = 'consoles/console_list.html'
    context_object_name = 'consoles'
    paginate_by = 20

class ConsoleDetailView(UserMixin, DetailView):
    model = Console
    template_name = 'consoles/console.html'
    context_object_name = 'console'

class ConsoleUpdateView(UpdateView):
    model = Console
    template_name = 'core/update.html'
    form_class = ConsoleUpdateForm

class ConsoleCreateView(CreateView):
    model = Console
    fields = '__all__'
    template_name = 'core/create.html'

class ConsoleDeleteView(DeleteView):
    model = Console
    template_name = 'core/delete.html'
    success_url = reverse_lazy('consoles:list')

class BaseConsoleListView(UserMixin, ListView):
    model = BaseConsole
    template_name = 'consoles/baseconsole_list.html'
    context_object_name = 'baseconsoles'
    paginate_by = 20

class BaseConsoleDetailView(UserMixin, DetailView):
    model = BaseConsole
    template_name = 'consoles/baseconsole.html'
    context_object_name = 'baseconsole'

class BaseConsoleUpdateView(UpdateView):
    model = BaseConsole
    template_name = 'core/update.html'
    form_class = BaseConsoleUpdateForm

class BaseConsoleDeleteView(DeleteView):
    model = BaseConsole
    template_name = 'core/delete.html'
    success_url = reverse_lazy('console-list')