from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ScheduleAPIView.as_view(), name='schedule'),
]