from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HistoryAPIView.as_view(), name='history'),
    url(r'^(?P<pk>[0-9]+)/$', HistoryDetailAPIView.as_view(), name='history_detail'),
]

