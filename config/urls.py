from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import HomeView, UserCollectionView
from gameboyz.games.views import BaseGameListView, BaseGameDetailView, BaseGameUpdateView, BaseGameDeleteView
from gameboyz.consoles.views import BaseConsoleListView, BaseConsoleDetailView, BaseConsoleUpdateView, BaseConsoleDeleteView, ConsoleCreateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    # base game urls
    url(r'^basegames/$', BaseGameListView.as_view(), name='basegame-list'),
    url(r'^basegames/(?P<pk>\d+)/$', BaseGameDetailView.as_view(), name='basegame-detail'),
    url(r'^basegames/(?P<pk>\d+)/update/$', BaseGameUpdateView.as_view(), name='basegame-update'),
    url(r'^basegames/(?P<pk>\d+)/delete/$', BaseGameDeleteView.as_view(), name='basegame-delete'),
    # base console urls
    url(r'^baseconsoles/$', BaseConsoleListView.as_view(), name='baseconsole-list'),
    url(r'^baseconsoles/(?P<pk>\d+)/$', BaseConsoleDetailView.as_view(), name='baseconsole-detail'),
    url(r'^baseconsoles/(?P<pk>\d+)/add/$', ConsoleCreateView.as_view(), name='console-create'),
    url(r'^baseconsoles/(?P<pk>\d+)/update/$', BaseConsoleUpdateView.as_view(), name='baseconsole-update'),
    url(r'^baseconsoles/(?P<pk>\d+)/delete/$', BaseConsoleDeleteView.as_view(), name='baseconsole-delete'),
    # rest of the includes
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^games/', include('gameboyz.games.urls', namespace='games')),
    url(r'^consoles/', include('gameboyz.consoles.urls', namespace='consoles')),
    # user page
    url(r'^users/(?P<username>[-\w.+@]+)/$', UserCollectionView.as_view(), name='collection'),

]
