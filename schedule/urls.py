from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^group/$', GroupFilterByFaculty.as_view(), name="group_by_faculty"),
    url(r'^teacher/(?P<teacher>.+)/$', ScheduleOFTeacherAPIView.as_view(), name='teacher'),
    url(r'^group/(?P<group>.+)/$', ScheduleOFGroupAPIView.as_view(), name='group'),
]
