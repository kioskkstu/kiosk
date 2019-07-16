from django.test import TestCase
from .models import *
from university.models import *
from rest_framework import status
from django.urls import reverse


class ScheduleModelTests(TestCase):
    @classmethod
    def setUp(self):
        self.old_cnt_subject = Subject.objects.count()
        self.old_cnt_schedule = Schedule.objects.count()

        self.department = Department.objects.create(name='test', about='test')
        self.building = Building.objects.create(name='1', location='1', floor='1')

        self.subject = Subject.objects.create(name='test')

        self.teacher = Teacher.objects.create(name='test', photo='', status='test', contact='email',
                                              department=self.department)
        self.classroom = Classroom.objects.create(name='test', floor='1', about='test',
                                                  building=self.building)
        self.group = Group.objects.create(name='test', department=self.department)

        self.schedule = Schedule.objects.create(time='1', day_of_week='1', week='1', type='1', teacher=self.teacher,
                                                classroom=self.classroom, subject=self.subject,
                                                group=self.group)

    def test_model_create_Subject(self):
        self.new_cnt = Subject.objects.count()
        self.assertNotEqual(self.old_cnt_subject, self.new_cnt)

    def test_model_create_Schedule(self):
        self.new_cnt = Schedule.objects.count()
        self.assertNotEqual(self.old_cnt_schedule, self.new_cnt)

    def test_api_get_ScheduleOFTeacher(self):
        response = self.client.get(
            reverse('teacher'),
            kwargs={'teacher': self.teacher.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.teacher)

    def test_api_get_ScheduleOFGroup(self):
        response = self.client.get(
            reverse('group'),
            kwargs={'group': self.group.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.group)
