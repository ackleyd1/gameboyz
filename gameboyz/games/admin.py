from django.contrib import admin

from gameboyz.sales.models import Sale
from .models import BaseGame, Game, Theme, Keyword, Franchise, Collection

class SaleInline(admin.StackedInline):
    model = Sale
    extra = 1

class GameAdmin(admin.ModelAdmin):
    inlines = [SaleInline,]

admin.site.register(BaseGame)
admin.site.register(Game, GameAdmin)
admin.site.register(Theme)
admin.site.register(Keyword)
admin.site.register(Franchise)
admin.site.register(Collection)
