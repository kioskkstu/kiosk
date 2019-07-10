from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^history/$', HistoryAPIView.as_view(), name='history'),
    url(r'^history/(?P<pk>[0-9]+)/$', HistoryDetailAPIView.as_view(), name='history_detail'),
]