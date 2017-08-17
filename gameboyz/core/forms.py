from django import forms
from django.apps import apps

from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Prevents a circular import
Game = apps.get_model('games', 'Game')

class CrispyLoginForm(LoginForm):
    """Creates a crispy LoginForm with the crispy FormHelper"""
    def __init__(self, *args, **kwargs):
        super(CrispyLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('login', 'Login'))

class CrispySignupForm(SignupForm):
    """Creates a crispy Signup with the crispy FormHelper"""
    def __init__(self, *args, **kwargs):
        super(CrispySignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('signup', 'Signup'))
