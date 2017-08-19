from django.conf.urls import url

from .adminviews import BaseConsoleList, BaseConsoleCreate, BaseConsoleDetail, BaseConsoleUpdate, BaseConsoleDelete, ConsoleCreate, ConsoleDetail, ConsoleUpdate, ConsoleDelete

urlpatterns = [
    url(r'^$', BaseConsoleList.as_view(), name='list'),
    url(r'^create/$', BaseConsoleCreate.as_view(), name='create'),
    url(r'^(?P<baseconsole_pk>\d+)/$', BaseConsoleDetail.as_view(), name='detail'),
    url(r'^(?P<baseconsole_pk>\d+)/update/$', BaseConsoleUpdate.as_view(), name='update'),
    url(r'^(?P<baseconsole_pk>\d+)/delete/$', BaseConsoleDelete.as_view(), name='delete'),
    url(r'^(?P<baseconsole_pk>\d+)/create/$', ConsoleCreate.as_view(), name='consoles-create'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/$', ConsoleDetail.as_view(), name='consoles-detail'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/update/$', ConsoleUpdate.as_view(), name='consoles-update'),
    url(r'^(?P<baseconsole_pk>\d+)/(?P<console_pk>\d+)/delete/$', ConsoleDelete.as_view(), name='consoles-delete'),
]