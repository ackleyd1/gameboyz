from django.contrib import admin

from gameboyz.sales.models import Sale

from .models import BaseGame, Game, GameListing, Keyword, Franchise, Collection

class GameListingInline(admin.StackedInline):
    model = GameListing
    extra = 1

class SaleInline(admin.StackedInline):
    model = Sale
    extra = 0

class GameAdmin(admin.ModelAdmin):
    inlines = [SaleInline, GameListingInline]

admin.site.register(BaseGame)
admin.site.register(Game, GameAdmin)
admin.site.register(GameListing)
admin.site.register(Keyword)
admin.site.register(Franchise)
admin.site.register(Collection)
