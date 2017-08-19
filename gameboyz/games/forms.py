from django import forms
from django.apps import apps

BaseGame = apps.get_model('games', 'BaseGame')
Game = apps.get_model('games', 'Game')
GameListing = apps.get_model('games', 'GameListing')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BaseGameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = BaseGame
        fields = '__all__'

class GameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Game
        fields = ['basegame', 'slug', 'edition', 'baseconsole', 'asin', 'epid', 'image', 'published']

class GameListingUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = GameListing
        fields = ['price', 'condition']

class BraintreeSaleForm(forms.Form):
    payment_method_nonce = forms.CharField()