from django import forms
from django.apps import apps

BaseConsole = apps.get_model('consoles', 'BaseConsole')
Console = apps.get_model('consoles', 'Console')

class BaseConsoleUpdateForm(forms.ModelForm):
    class Meta:
        model = BaseConsole
        fields = '__all__'

class ConsoleCreateForm(forms.ModelForm):
    class Meta:
        model = Console
        fields = ['edition', 'asin', 'epid', 'image', 'published']

class ConsoleUpdateForm(forms.ModelForm):
    class Meta:
        model = Console
        fields = '__all__'