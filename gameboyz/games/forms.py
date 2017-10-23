from django import forms
from django.apps import apps

BaseGame = apps.get_model('games', 'BaseGame')
Game = apps.get_model('games', 'Game')
GameListing = apps.get_model('games', 'GameListing')

class BaseGameUpdateForm(forms.ModelForm):
    class Meta:
        model = BaseGame
        fields = '__all__'

class GameUpdateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['basegame', 'slug', 'edition', 'baseconsole', 'asin', 'epid', 'image', 'published']

class GameListingUpdateForm(forms.ModelForm):
    class Meta:
        model = GameListing
        fields = ['price', 'condition']

class GameListingCreateForm(forms.ModelForm):
    images = forms.ImageField(label='Image of your game', required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = GameListing
        fields = ['price', 'condition']

class BraintreeSaleForm(forms.Form):
    payment_method_nonce = forms.CharField()