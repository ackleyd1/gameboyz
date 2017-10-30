from django.conf.urls import url

from .views import SaleSummaryView

urlpatterns = [
    url(r'^$', SaleSummaryView.as_view(), name='overview'),
]