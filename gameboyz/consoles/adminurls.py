from django.conf.urls import url

from .adminviews import BaseConsoleListView, BaseConsoleCreateView, BaseConsoleDetailView, BaseConsoleUpdateView, BaseConsoleDeleteView, ConsoleCreateView, ConsoleDetailView, ConsoleUpdateView, ConsoleDeleteView

urlpatterns = [
    url(r'^$', BaseConsoleListView.as_view(), name='list'),
    url(r'^create/$', BaseConsoleCreateView.as_view(), name='create'),
    url(r'^(?P<baseconsole_pk>\d+)/$', BaseConsoleDetailView.as_view(), name='detail'),
    url(r'^(?P<baseconsole_pk>\d+)/update/$', BaseConsoleUpdateView.as_view(), name='update'),
    url(r'^(?P<baseconsole_pk>\d+)/delete/$', BaseConsoleDeleteView.as_view(), name='delete'),
    url(r'^(?P<baseconsole_pk>\d+)/create/$', ConsoleCreateView.as_view(), name='consoles-create'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/$', ConsoleDetailView.as_view(), name='consoles-detail'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/update/$', ConsoleUpdateView.as_view(), name='consoles-update'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/delete/$', ConsoleDeleteView.as_view(), name='consoles-delete'),
]