from django.conf.urls import url

from .adminviews import PlatformListView, PlatformCreateView, PlatformDetailView, PlatformUpdateView, PlatformDeleteView, ConsoleCreateView, ConsoleDetailView, ConsoleUpdateView, ConsoleDeleteView

urlpatterns = [
    url(r'^$', PlatformListView.as_view(), name='list'),
    url(r'^create/$', PlatformCreateView.as_view(), name='create'),
    url(r'^(?P<platform_pk>\d+)/$', PlatformDetailView.as_view(), name='detail'),
    url(r'^(?P<platform_pk>\d+)/update/$', PlatformUpdateView.as_view(), name='update'),
    url(r'^(?P<platform_pk>\d+)/delete/$', PlatformDeleteView.as_view(), name='delete'),
    url(r'^(?P<platform_pk>\d+)/create/$', ConsoleCreateView.as_view(), name='consoles-create'),
    url(r'^(?P<platform_pk>\d+)/(?P<console_pk>\d+)/$', ConsoleDetailView.as_view(), name='consoles-detail'),
    url(r'^(?P<platform_pk>\d+)/(?P<console_pk>\d+)/update/$', ConsoleUpdateView.as_view(), name='consoles-update'),
    url(r'^(?P<platform_pk>\d+)/(?P<console_pk>\d+)/delete/$', ConsoleDeleteView.as_view(), name='consoles-delete'),
]