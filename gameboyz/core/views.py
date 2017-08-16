from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import View

from gameboyz.consoles.models import BaseConsole
from gameboyz.games.models import Game

from .forms import CrispyLoginForm, CrispySignupForm

class UserMixin:
    """Mixin for Signup and Login on the navbar template."""
    def get_context_data(self, *args, **kwargs):
        context = super(UserMixin, self).get_context_data(*args, **kwargs)
        context['login_form'] = CrispyLoginForm()
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context

class NameSearchMixin:
    """ViewMixin to search a ListView by a model's name field."""
    def get_context_data(self, *args, **kwargs):
        """Extends the context with search set to True for the navbar template search."""
        context = super(NameSearchMixin, self).get_context_data(*args, **kwargs)
        context['search'] = True
        return context

    def get_queryset(self, *args, **kwargs):
        """Filters the queryset by the user's query."""
        queryset = super(NameSearchMixin, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(basegame__name__icontains=q)
        return queryset

class HomeView(View):
    """
    HomeView for the website.
    **Template:**
    :template:`core/home.html`
    """
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        """Handles the HomeView's get request."""
        return render(request, self.template_name, self.get_context_data(*args, **kwargs))

    def get_context_data(self, *args, **kwargs):
        """Implements the UserMixin context data."""
        context = {'login_form': CrispyLoginForm()}
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context


