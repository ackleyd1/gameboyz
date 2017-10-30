from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import StaffRequiredMixin

from .models import Platform, Console
from .forms import PlatformUpdateForm, ConsoleCreateForm, ConsoleUpdateForm

##########################################################
# Platform Admin Views (Detail shows List of Consoles)
##########################################################

class PlatformListView(StaffRequiredMixin, ListView):
    model = Platform
    template_name = 'consoles/admin/platform_list.html'
    context_object_name = 'platforms'
    paginate_by = 20

class PlatformCreateView(StaffRequiredMixin, CreateView):
    model = Platform
    template_name = 'core/create.html'
    fields = '__all__'

    def get_success_url(self):
      return reverse('platforms:detail', kwargs={'platform_pk': self.object.pk})

class PlatformDetailView(StaffRequiredMixin, DetailView):
    model = Platform
    template_name = 'consoles/admin/platform.html'
    context_object_name = 'platform'
    pk_url_kwarg = 'platform_pk'

class PlatformUpdateView(StaffRequiredMixin, UpdateView):
    model = Platform
    template_name = 'core/update.html'
    form_class = PlatformUpdateForm
    pk_url_kwarg = 'platform_pk'

    def get_success_url(self):
        return reverse('platforms:detail', kwargs={'platform_pk': self.object.pk})

class PlatformDeleteView(StaffRequiredMixin, DeleteView):
    model = Platform
    template_name = 'core/delete.html'
    success_url = reverse_lazy('platforms:list')
    pk_url_kwarg = 'platform_pk'

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
        return reverse('platforms:consoles-detail', kwargs={'platform_pk': self.object.platform.pk, 'console_pk': self.object.pk})

class ConsoleCreateView(StaffRequiredMixin, CreateView):
    model = Console
    form_class = ConsoleCreateForm
    template_name = 'core/create.html'

    def get_success_url(self):
        return reverse('platforms:consoles-detail', kwargs={'platform_pk': self.object.platform.pk, 'console_pk': self.object.pk})

    def form_valid(self, form):
        console = form.save(commit=False)
        console.platform = Platform.objects.get(pk=self.kwargs.get('platform_pk'))
        self.object = console.save()
        return super().form_valid(form)

class ConsoleDeleteView(StaffRequiredMixin, DeleteView):
    model = Console
    template_name = 'core/delete.html'
    pk_url_kwarg = 'console_pk'

    def get_success_url(self):
        return reverse('platforms:detail', kwargs={'platform_pk': self.object.platform.pk})
