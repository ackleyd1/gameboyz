from django.conf.urls import url

from .adminviews import GameTitleListView, GameTitleCreateView, GameTitleDetailView, GameTitleUpdateView, GameTitleDeleteView, GameCreateView, GameDetailView, GameUpdateView, GameDeleteView

urlpatterns = [
    url(r'^$', GameTitleListView.as_view(), name='list'),
    url(r'^create/$', GameTitleCreateView.as_view(), name='create'),
    url(r'^(?P<gametitle_pk>\d+)/$', GameTitleDetailView.as_view(), name='detail'),
    url(r'^(?P<gametitle_pk>\d+)/update/$', GameTitleUpdateView.as_view(), name='update'),
    url(r'^(?P<gametitle_pk>\d+)/delete/$', GameTitleDeleteView.as_view(), name='delete'),
    url(r'^(?P<gametitle_pk>\d+)/create/$', GameCreateView.as_view(), name='games-create'),
    url(r'^(?P<gametitle_pk>\d+)/(?P<game_pk>\d+)/$', GameDetailView.as_view(), name='games-detail'),
    url(r'^(?P<gametitle_pk>\d+)/(?P<game_pk>\d+)/update/$', GameUpdateView.as_view(), name='games-update'),
    url(r'^(?P<gametitle_pk>\d+)/(?P<game_pk>\d+)/delete/$', GameDeleteView.as_view(), name='games-delete'),
]