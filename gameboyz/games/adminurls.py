from django.conf.urls import url

from .adminviews import BaseGameList, BaseGameCreate, BaseGameDetail, BaseGameUpdate, BaseGameDelete, GameCreate, GameDetail, GameUpdate, GameDelete

urlpatterns = [
    url(r'^$', BaseGameList.as_view(), name='list'),
    url(r'^create/$', BaseGameCreate.as_view(), name='create'),
    url(r'^(?P<basegame_pk>\d+)/$', BaseGameDetail.as_view(), name='detail'),
    url(r'^(?P<basegame_pk>\d+)/update/$', BaseGameUpdate.as_view(), name='update'),
    url(r'^(?P<basegame_pk>\d+)/delete/$', BaseGameDelete.as_view(), name='delete'),
    url(r'^(?P<basegame_pk>\d+)/create/$', GameCreate.as_view(), name='games-create'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/$', GameDetail.as_view(), name='games-detail'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/update/$', GameUpdate.as_view(), name='games-update'),
    url(r'^(?P<basegame_pk>\d+)/(?P<game_pk>\d+)/delete/$', GameDelete.as_view(), name='games-delete'),
]