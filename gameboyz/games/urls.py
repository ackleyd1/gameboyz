from django.conf.urls import url

from .views import GameListView, GameDetailView, GameUpdateView, GameDeleteView, GameListingCreateView

urlpatterns = [
    url(r'^$', GameListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', GameDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', GameUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', GameDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/sell/$', GameListingCreateView.as_view(), name='listing_create')

]