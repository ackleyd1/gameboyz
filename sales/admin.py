from django.contrib import admin

from sales.models import GameSale, ConsoleSale

admin.site.register(GameSale)
admin.site.register(ConsoleSale)

