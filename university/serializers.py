from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'photo', 'status', 'contact',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'grade',)


class PreUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreUniversity
        fields = ('id', 'name', 'about',)


class DepartmentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'about', 'teachers', 'groups',)


class FacultySerializer(serializers.ModelSerializer):
    departments_of_faculty = DepartmentSerializer(many=True)

    class Meta:
        model = Faculty
        fields = ('id', 'name', 'about', 'departments_of_faculty',)


class InstituteSerializer(serializers.ModelSerializer):
    departments_of_institute = DepartmentSerializer(many=True)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'about', 'departments_of_institute',)


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'name', 'floor', 'about',)


class BuildingSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True)

    class Meta:
        model = Building
        fields = ('id', 'name', 'floor', 'classrooms')





