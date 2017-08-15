from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from gameboyz.core.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^games/', include('gameboyz.games.urls', namespace='games'))

]
