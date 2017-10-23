from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import Home, UserCollection, BaseConsoleOverview

from gameboyz.games.views import GameList, GameDetail, GameListingDetail, GameListingCreate, GameListingUpdate, GameListingDelete
from gameboyz.consoles.views import ConsoleList

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^basegames/', include('gameboyz.games.adminurls', namespace='basegames')),
    url(r'^baseconsoles/', include('gameboyz.consoles.adminurls', namespace='baseconsoles')),
    url(r'sales/', include('gameboyz.sales.adminurls', namespace='sales')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    # User urls
    url(
        regex=r'^users/(?P<username>[-\w.+@]+)/$',
        view=UserCollection.as_view(),
        name='collection'
    ),
    # Overview
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/$',
        view=BaseConsoleOverview.as_view(),
        name='overview'
    ),
    # Game urls
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/$',
        view=GameList.as_view(),
        name='games'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/$',
        view=GameDetail.as_view(),
        name='games-detail'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/create/$',
        view=GameListingCreate.as_view(),
        name='gamelistings-create'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/$',view=GameListingDetail.as_view(),
        name='gamelistings-detail'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/update/$',view=GameListingUpdate.as_view(),
        name='gamelistings-update'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/delete/$',view=GameListingDelete.as_view(),
        name='gamelistings-delete'
    ),
    # Console urls
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/consoles/$',
        view=ConsoleList.as_view(),
        name='consoles'
    ),
    # Accessory urls

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns