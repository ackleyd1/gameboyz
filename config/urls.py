from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import HomeView, BaseConsoleOverviewView, UserCollectionView

from gameboyz.games.views import GameListView, GameDetailView, GameListingDetailView, GameListingCreateView, GameListingUpdateView, GameListingDeleteView
from gameboyz.consoles.views import ConsoleListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^basegames/', include('gameboyz.games.adminurls', namespace='basegames')),
    url(r'^baseconsoles/', include('gameboyz.consoles.adminurls', namespace='baseconsoles')),
    url(r'sales/', include('gameboyz.sales.adminurls', namespace='sales')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    # User urls
    url(
        regex=r'^users/(?P<username>[-\w.+@]+)/$',
        view=UserCollectionView.as_view(),
        name='collection'
    ),
    # Overview
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/$',
        view=BaseConsoleOverviewView.as_view(),
        name='overview'
    ),
    # Game urls
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/$',
        view=GameListView.as_view(),
        name='games'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/$',
        view=GameDetailView.as_view(),
        name='games-detail'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/create/$',
        view=GameListingCreateView.as_view(),
        name='gamelistings-create'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/$',view=GameListingDetailView.as_view(),
        name='gamelistings-detail'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/update/$',view=GameListingUpdateView.as_view(),
        name='gamelistings-update'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_pk>\d+)/delete/$',view=GameListingDeleteView.as_view(),
        name='gamelistings-delete'
    ),
    # Console urls
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/consoles/$',
        view=ConsoleListView.as_view(),
        name='consoles'
    ),
    # Accessory urls

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns