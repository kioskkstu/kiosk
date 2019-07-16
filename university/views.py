from rest_framework import generics
from .models import *

from .serializers import *


class PreUniversityAPIView(generics.ListAPIView):
    queryset = PreUniversity.objects.all()
    serializer_class = PreUniversitySerializer


class DepartmentAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FacultyAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class InstituteAPIView(generics.ListAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class BuildingAPIView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class ClassroomAPIView(generics.ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class GroupAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PreUniversityDetailAPIView(generics.RetrieveAPIView):
    queryset = PreUniversity.objects.all()
    serializer_class = PreUniversitySerializer


class DepartmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FacultyDetailAPIView(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class InstituteDetailAPIView(generics.RetrieveAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
