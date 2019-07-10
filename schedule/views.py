from rest_framework import generics
from .models import *
from .serializers import *


class SubjectAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ScheduleOfGroupAPIView(generics.ListAPIView):
    queryset = ScheduleOfGroup.objects.all()
    serializer_class = ScheduleOfGroupSerializer


class ScheduleOfTeacherAPIView(generics.ListAPIView):
    queryset = ScheduleOfTeacher.objects.all()
    serializer_class = ScheduleOfTeacherSerializer
