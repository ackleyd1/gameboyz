from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import HomeView, VerifyView
from gameboyz.consoles.views import ConsoleView, ConsoleVerifyView
from gameboyz.games.views import GameView, GameVerifyView, GameDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    
    url(r'^verify/$', VerifyView.as_view(), name='verify'),
    url(r'^verify/(?P<console_slug>[-\w]+)/$', ConsoleVerifyView.as_view(), name='console_verify'),
    url(r'^verify/(?P<console_slug>[-\w]+)/(?P<game_slug>[-\w]+)/verify/$', GameVerifyView.as_view(), name='game_verify'),
    url(r'^verify/(?P<console_slug>[-\w]+)/(?P<game_slug>[-\w]+)/delete/$', GameDeleteView.as_view(), name='game_delete'),
    
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<console_slug>[-\w]+)/$', ConsoleView.as_view(), name='console'),
    url(r'^(?P<console_slug>[-\w]+)/(?P<game_slug>[-\w]+)/$', GameView.as_view(), name='game'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
