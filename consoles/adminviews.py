from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import StaffRequiredMixin

from .models import BaseConsole, Console
from .forms import BaseConsoleUpdateForm, ConsoleCreateForm, ConsoleUpdateForm

##########################################################
# BaseConsole Admin Views (Detail shows List of Consoles)
##########################################################

class BaseConsoleListView(StaffRequiredMixin, ListView):
    model = BaseConsole
    template_name = 'consoles/admin/baseconsole_list.html'
    context_object_name = 'baseconsoles'
    paginate_by = 20

class BaseConsoleCreateView(StaffRequiredMixin, CreateView):
    model = BaseConsole
    template_name = 'core/create.html'
    fields = '__all__'

    def get_success_url(self):
      return reverse('baseconsoles:detail', kwargs={'baseconsole_pk': self.object.pk})

class BaseConsoleDetailView(StaffRequiredMixin, DetailView):
    model = BaseConsole
    template_name = 'consoles/admin/baseconsole.html'
    context_object_name = 'baseconsole'
    pk_url_kwarg = 'baseconsole_pk'

class BaseConsoleUpdateView(StaffRequiredMixin, UpdateView):
    model = BaseConsole
    template_name = 'core/update.html'
    form_class = BaseConsoleUpdateForm
    pk_url_kwarg = 'baseconsole_pk'

    def get_success_url(self):
        return reverse('baseconsoles:detail', kwargs={'baseconsole_pk': self.object.pk})

class BaseConsoleDeleteView(StaffRequiredMixin, DeleteView):
    model = BaseConsole
    template_name = 'core/delete.html'
    success_url = reverse_lazy('baseconsoles:list')
    pk_url_kwarg = 'baseconsole_pk'

##########################################################
# Console Admin Views
##########################################################

class ConsoleDetailView(StaffRequiredMixin, DetailView):
    model = Console
    template_name = 'consoles/admin/console.html'
    context_object_name = 'console'
    pk_url_kwarg = 'console_pk'

class ConsoleUpdateView(StaffRequiredMixin, UpdateView):
    model = Console
    template_name = 'core/update.html'
    form_class = ConsoleUpdateForm
    pk_url_kwarg = 'console_pk'

    def get_success_url(self):
        return reverse('baseconsoles:consoles-detail', kwargs={'baseconsole_pk': self.object.baseconsole.pk, 'console_pk': self.object.pk})

class ConsoleCreateView(StaffRequiredMixin, CreateView):
    model = Console
    form_class = ConsoleCreateForm
    template_name = 'core/create.html'

    def get_success_url(self):
        return reverse('baseconsoles:consoles-detail', kwargs={'baseconsole_pk': self.object.baseconsole.pk, 'console_pk': self.object.pk})

    def form_valid(self, form):
        console = form.save(commit=False)
        console.baseconsole = BaseConsole.objects.get(pk=self.kwargs.get('baseconsole_pk'))
        self.object = console.save()
        return super().form_valid(form)

class ConsoleDeleteView(StaffRequiredMixin, DeleteView):
    model = Console
    template_name = 'core/delete.html'
    pk_url_kwarg = 'console_pk'

    def get_success_url(self):
        return reverse('baseconsoles:detail', kwargs={'baseconsole_pk': self.object.baseconsole.pk})
