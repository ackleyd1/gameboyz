from django.contrib import admin

from gameboyz.sales.models import GameSale

from .models import BaseGame, Game, GameListing, Keyword, Franchise, Collection

class GameListingInline(admin.StackedInline):
    model = GameListing
    extra = 1

class GameSaleInline(admin.StackedInline):
    model = GameSale
    extra = 0

class GameAdmin(admin.ModelAdmin):
    inlines = [GameSaleInline, GameListingInline]

admin.site.register(BaseGame)
admin.site.register(Game, GameAdmin)
admin.site.register(GameListing)
admin.site.register(Keyword)
admin.site.register(Franchise)
admin.site.register(Collection)
