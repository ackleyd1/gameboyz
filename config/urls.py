from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import HomeView, UserCollectionView, BaseConsoleOverviewView
from gameboyz.games.views import GameListView, GameDetailView, GameListingDetailView, GameListingCreateView, GameListingUpdateView, GameListingDeleteView
from gameboyz.consoles.views import ConsoleListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^gametitles/', include('gameboyz.games.adminurls', namespace='gametitles')),
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
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_id>[^/]+)/$',view=GameListingDetailView.as_view(),
        name='gamelistings-detail'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_id>[^/]+)/update/$',view=GameListingUpdateView.as_view(),
        name='gamelistings-update'
    ),
    url(
        regex=r'^(?P<baseconsole_slug>[-\w]+)/games/(?P<game_slug>[-\w]+)/(?P<gamelisting_id>[^/]+)/delete/$',view=GameListingDeleteView.as_view(),
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
