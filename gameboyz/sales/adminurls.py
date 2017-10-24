from django.conf.urls import url

from .adminviews import SaleSummaryView

urlpatterns = [
    url(r'^$', SaleSummaryView.as_view(), name='overview'),
]