from rest_framework import serializers
from .models import *


class PreUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreUniversity
        fields = ('name', 'about',)


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name', 'about',)


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('name', 'about',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'about', 'faculty', 'institute',)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'photo', 'status', 'contact', 'department',)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('name', 'location', 'floor',)


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('name', 'floor', 'about',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'department',)
