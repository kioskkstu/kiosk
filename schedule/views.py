from rest_framework import generics

from .serializers import *


class SubjectAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ScheduleOFTeacherAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        teacher = self.kwargs['teacher']
        return Schedule.objects.filter(teacher=teacher)


class ScheduleOFGroupAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        group = self.kwargs['group']
        return Schedule.objects.filter(group=group)
