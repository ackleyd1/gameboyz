from django.conf.urls import url

from .adminviews import SaleSummaryView

from gameboyz.sales.api.views import SaleListView

urlpatterns = [
    url(r'^$', SaleSummaryView.as_view(), name='overview'),
    url(r'^api/v1/$', SaleListView.as_view(), name='api-overview'),
]