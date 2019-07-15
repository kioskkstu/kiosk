from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'photo', 'status', 'contact',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class PreUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreUniversity
        fields = ('name', 'about',)


class DepartmentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = Department
        fields = ('name', 'about', 'teachers', 'groups',)


class FacultySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Faculty
        fields = ('name', 'about', 'department',)


class InstituteSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Institute
        fields = ('name', 'about', 'department',)


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('name', 'floor', 'about',)


class BuildingSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True)

    class Meta:
        model = Building
        fields = ('name', 'location', 'floor', 'classrooms')





