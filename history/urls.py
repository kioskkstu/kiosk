from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from .views import *

urlpatterns = [
    url(r'^$', HistoryAPIView.as_view(), name='history'),
    url(r'^(?P<pk>[0-9]+)/$', HistoryDetailAPIView.as_view(), name='history_detail'),
]
