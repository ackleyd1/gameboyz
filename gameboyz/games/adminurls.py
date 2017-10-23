from django.conf.urls import url

from .adminviews import BaseGameListView, BaseGameCreateView, BaseGameDetailView, BaseGameUpdateView, BaseGameDeleteView, GameCreateView, GameDetailView, GameUpdateView, GameDeleteView

urlpatterns = [
    url(r'^$', BaseGameListView.as_view(), name='list'),
    url(r'^create/$', BaseGameCreateView.as_view(), name='create'),
    url(r'^(?P<basegame_pk>\d+)/$', BaseGameDetailView.as_view(), name='detail'),
    url(r'^(?P<basegame_pk>\d+)/update/$', BaseGameUpdateView.as_view(), name='update'),
    url(r'^(?P<basegame_pk>\d+)/delete/$', BaseGameDeleteView.as_view(), name='delete'),
    url(r'^(?P<basegame_pk>\d+)/create/$', GameCreateView.as_view(), name='games-create'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/$', GameDetailView.as_view(), name='games-detail'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/update/$', GameUpdateView.as_view(), name='games-update'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/delete/$', GameDeleteView.as_view(), name='games-delete'),
]