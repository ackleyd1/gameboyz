from django.conf.urls import url, include

from .views import game_list, GameDetailView, GameUpdateView, GameDeleteView

urlpatterns = [
    url(r'^$', game_list, name='list'),
    url(r'^(?P<pk>\d+)/$', GameDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', GameUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', GameDeleteView.as_view(), name='delete')

]