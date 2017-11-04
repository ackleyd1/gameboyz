from django.conf.urls import url

from .views import  GameListView, GameCreateView, GameDetailView, GameUpdateView, GameDeleteView

urlpatterns = [
    url(r'^$', GameListView.as_view(), name='games-list'),
    url(r'^create/$', GameCreateView.as_view(), name='games-create'),
    url(r'^(?P<game_pk>\d+)/$', GameDetailView.as_view(), name='games-detail'),
    url(r'^(?P<game_pk>\d+)/update/$', GameUpdateView.as_view(), name='games-update'),
    url(r'^(?P<game_pk>\d+)/delete/$', GameDeleteView.as_view(), name='games-delete'),
]