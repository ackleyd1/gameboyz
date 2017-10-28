from django import forms
from django.apps import apps

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

BaseConsole = apps.get_model('consoles', 'BaseConsole')
Console = apps.get_model('consoles', 'Console')

class BaseConsoleUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = BaseConsole
        fields = '__all__'

class ConsoleCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Console
        fields = ['edition', 'asin', 'epid', 'image', 'published']

class ConsoleUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = Console
        fields = '__all__'