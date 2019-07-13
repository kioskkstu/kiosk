from university.serializers import *
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )


class ScheduleSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer()
    teachers = TeacherSerializer()
    classrooms = ClassroomSerializer()
    groups = GroupSerializer()

    class Meta:
        model = Schedule
        fields = ('time', 'day_of_week', 'subjects', 'week', 'type', 'teachers', 'classrooms', 'groups',)
