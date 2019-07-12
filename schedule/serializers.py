from rest_framework import serializers

from university.serializers import *
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )


class ScheduleOfGroupSerializer(serializers.ModelSerializer):
    subject_for_group = SubjectSerializer()
    teachers_for_group = TeacherSerializer()
    classroom_for_group = ClassroomSerializer()
    schedule_of_group = GroupSerializer()

    class Meta:
        model = ScheduleOfGroup
        fields = ('time', 'day_of_week', 'subject', 'week', 'type', 'teacher', 'classroom', )


class ScheduleOfTeacherSerializer(serializers.ModelSerializer):
    subject_for_teacher = SubjectSerializer()
    teachers_for_schedule = TeacherSerializer()
    classroom_for_schedule = ClassroomSerializer()
    schedule_of_teacher = GroupSerializer()

    class Meta:
        model = ScheduleOfTeacher
        fields = ('time', 'day_of_week', 'subject', 'week', 'type', 'group', 'classroom',)