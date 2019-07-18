from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^faculty/$', FacultyAPIView.as_view(), name='faculty'),
    url(r'^institute/$', InstituteAPIView.as_view(), name='institute'),
    url(r'^building/$', BuildingAPIView.as_view(), name='building'),
    url(r'^classroom/$', ClassroomAPIView.as_view(), name='classroom'),
    url(r'^group/$', GroupAPIView.as_view(), name='group'),
    url(r'^department/$', DepartmentAPIView.as_view(), name='department'),
    url(r'^teacher/$', TeacherAPIView.as_view(), name='teacher'),
    url(r'^preuniversity/$', PreUniversityAPIView.as_view(), name='preuniversity'),
    url(r'^preuniversity/(?P<pk>[0-9]+)/$', PreUniversityDetailAPIView.as_view(), name='preuniversity_detail'),
    url(r'^faculty/(?P<pk>[0-9]+)/$', FacultyDetailAPIView.as_view(), name='faculty_detail'),
    url(r'^institute/(?P<pk>[0-9]+)/$', InstituteDetailAPIView.as_view(), name='institute_detail'),
    url(r'^department/(?P<pk>[0-9]+)/$', DepartmentDetailAPIView.as_view(), name='department_detail'),
]