from django import forms
from django.apps import apps
from django.urls import reverse


Game = apps.get_model('games', 'Game')

from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CrispyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CrispyLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class CrispySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CrispySignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
