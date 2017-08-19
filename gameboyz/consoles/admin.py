from django.contrib import admin

from .models import BaseConsole, Console

admin.site.register(BaseConsole)
admin.site.register(Console)
