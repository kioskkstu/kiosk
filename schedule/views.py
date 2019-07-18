from rest_framework import generics

from .serializers import *


class SubjectAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ScheduleOFTeacherAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        teacher = self.kwargs['teacher']
        queryset = Schedule.objects.filter(teacher=teacher)
        faculty = self.request.query_params.get('faculty', None)
        if faculty is not None:
            queryset = queryset.filter(purchaser__username=username)
        grade = self.request.query_params.get('grade', None)
        group = self.request.query_params.get('group', None)
        return queryset

# serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Purchase.objects.all()
#         username = self.request.query_params.get('username', None)
#         if username is not None:
#             queryset = queryset.filter(purchaser__username=username)
#         return queryset


class ScheduleOFGroupAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        group = self.kwargs['group']
        return Schedule.objects.filter(group=group)
