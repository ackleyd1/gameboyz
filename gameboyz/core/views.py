from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

from gameboyz.games.models import GameListing

from .mixins import UserMixin
from .forms import CrispyLoginForm, CrispySignupForm

class HomeView(UserMixin, TemplateView):
    """
    HomeView for the website.
    **Template:**
    :template:`core/home.html`
    """
    template_name = 'core/home.html'

class UserCollectionView(UserMixin, DetailView):
    """
    UserCollectionView to view users listed games, consoles, and accessories
    **Template**
    :template:'core/collection.html'
    """
    model = User
    template_name = 'core/collection.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

