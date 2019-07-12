from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^scheduleofgroup/$', ScheduleOfGroupAPIView.as_view(), name='scheduleofgroup'),
    url(r'^scheduleofteacher/$', ScheduleOfTeacherAPIView.as_view(), name='scheduleofteacher'),
]