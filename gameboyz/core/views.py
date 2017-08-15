from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import View

from .forms import CrispyLoginForm, CrispySignupForm

from gameboyz.consoles.models import BaseConsole
from gameboyz.games.models import Game

class UserMixin:
    def get_context_data(self, *args, **kwargs):
        context = super(UserMixin, self).get_context_data(*args, **kwargs)
        context['login_form'] = CrispyLoginForm()
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context

class NameSearchMixin:
    # Set search to true for the navbar template
    def get_context_data(self, *args, **kwargs):
        context = super(NameSearchMixin, self).get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    # Filter the queryset by the basegame__name__icontains the query
    def get_queryset(self, *args, **kwargs):
        queryset = super(NameSearchMixin, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(basegame__name__icontains=q)
        return queryset

# Home view for gameboyz
class HomeView(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(*args, **kwargs))

    # Can't extend the UserMixin so we must duplicate the code
    def get_context_data(self, *args, **kwargs):
        context = {'login_form': CrispyLoginForm()}
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context


