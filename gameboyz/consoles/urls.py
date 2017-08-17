from django.conf.urls import url

from .views import ConsoleListView, ConsoleDetailView, ConsoleUpdateView, ConsoleDeleteView

urlpatterns = [
    url(r'^$', ConsoleListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ConsoleDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', ConsoleUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ConsoleDeleteView.as_view(), name='delete')
]