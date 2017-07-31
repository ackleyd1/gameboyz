from django.contrib import admin

from .models import BaseGame, Game, Theme, Keyword, Franchise, Collection

admin.site.register(BaseGame)
admin.site.register(Game)
admin.site.register(Theme)
admin.site.register(Keyword)
admin.site.register(Franchise)
admin.site.register(Collection)
