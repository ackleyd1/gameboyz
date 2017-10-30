from django import forms
from django.apps import apps

GameTitle = apps.get_model('games', 'GameTitle')
Game = apps.get_model('games', 'Game')
GameListing = apps.get_model('games', 'GameListing')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class GameTitleUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = GameTitle
        fields = '__all__'

class GameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Game
        fields = ['gametitle', 'slug', 'edition', 'platform', 'asin', 'epid', 'image']

class GameListingUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = GameListing
        fields = ['price', 'condition']

class GameListingCreateForm(forms.ModelForm):
    images = forms.ImageField(label='Images of your game', required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = GameListing
        fields = ['price', 'condition']

class BraintreeSaleForm(forms.Form):
    payment_method_nonce = forms.CharField()