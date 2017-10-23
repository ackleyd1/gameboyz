from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gameboyz.core.mixins import UserMixin

from .models import Console

class ConsoleListView(UserMixin, ListView):
    model = Console
    template_name = 'consoles/console_list.html'
    context_object_name = 'consoles'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        consoles = super().get_queryset(*args, **kwargs)
        consoles = consoles.filter(baseconsole__slug=self.kwargs.get('baseconsole_slug'))
        q = self.request.GET.get('q')
        if q:
            consoles = consoles.filter(baseconsole__name__icontains=q)
        return consoles