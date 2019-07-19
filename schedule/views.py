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


class GroupFilterByFaculty(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = Group.objects.all()
        faculty = self.request.query_params.get('faculty', None)
        if faculty is not None:
            queryset = queryset.filter(department__faculty=faculty)
        return queryset


class ScheduleOFGroupAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        group = self.kwargs['group']
        return Schedule.objects.filter(group=group)
