from django.contrib import admin

from .models import Game, Theme, Keyword, Franchise, Collection, EbayListing


admin.site.register(Game)
admin.site.register(Theme)
admin.site.register(Keyword)
admin.site.register(Franchise)
admin.site.register(Collection)
admin.site.register(EbayListing)