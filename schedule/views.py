from rest_framework import generics

from .serializers import *


class SubjectAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ScheduleAPIView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
