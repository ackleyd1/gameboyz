from django import forms
from django.apps import apps


Game = apps.get_model('games', 'Game')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class GameUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GameUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Game
        fields = '__all__'