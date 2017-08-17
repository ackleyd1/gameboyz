from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gameboyz.consoles.models import BaseConsole
from gameboyz.games.models import Game

from .mixins import UserMixin
from .forms import CrispyLoginForm, CrispySignupForm

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
