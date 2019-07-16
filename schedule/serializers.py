from university.serializers import *
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    classroom = ClassroomSerializer()
    group = GroupSerializer()

    class Meta:
        model = Schedule
        fields = ('time', 'day_of_week', 'subject', 'week', 'type', 'teacher', 'classroom', 'group',)

