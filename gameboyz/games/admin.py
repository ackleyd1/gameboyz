from django.contrib import admin

from gameboyz.sales.models import GameSale

from .models import BaseGame, Game, Franchise

class GameSaleInline(admin.StackedInline):
    model = GameSale
    extra = 0

class GameAdmin(admin.ModelAdmin):
    inlines = [GameSaleInline]

admin.site.register(BaseGame)
admin.site.register(Game, GameAdmin)
admin.site.register(Franchise)
