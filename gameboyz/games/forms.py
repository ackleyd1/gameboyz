from django import forms
from django.apps import apps

Game = apps.get_model('games', 'Game')
BaseGame = apps.get_model('games', 'BaseGame')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class GameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GameUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Game
        fields = ['basegame', 'slug', 'edition', 'console', 'asin', 'epid', 'image', 'published']

class BaseGameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseGameUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = BaseGame
        fields = '__all__'

class BraintreeSaleForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=20)
    payment_method_nonce = forms.CharField()