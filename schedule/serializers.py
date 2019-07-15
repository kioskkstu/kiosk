from university.serializers import *
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )


class ScheduleSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=False)
    classrooms = ClassroomSerializer(many=False)
    subjects = SubjectSerializer(many=False)
    groups = GroupSerializer(many=False)

    class Meta:
        model = Schedule
        fields = ('time', 'day_of_week', 'week', 'type', 'teachers', 'classrooms', 'subjects', 'groups', )