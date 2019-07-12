from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^group/$', ScheduleOfGroupAPIView.as_view(), name='scheduleofgroup'),
    url(r'^teacher/$', ScheduleOfTeacherAPIView.as_view(), name='scheduleofteacher'),
]