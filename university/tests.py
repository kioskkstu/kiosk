from django.test import TestCase
from .models import *
from rest_framework import status
from django.urls import reverse


# Create your tests here.
class UniversityModelTests(TestCase):
    @classmethod
    def setUp(self):
        self.old_cnt1 = PreUniversity.objects.count()
        self.old_cnt2 = Department.objects.count()
        self.old_cnt3 = Faculty.objects.count()
        self.old_cnt4 = Institute.objects.count()
        self.old_cnt5 = Teacher.objects.count()
        self.old_cnt6 = Building.objects.count()
        self.old_cnt7 = Classroom.objects.count()
        self.old_cnt8 = Group.objects.count()
        self.preuniversity = PreUniversity.objects.create(name='test', about='test')
        self.department = Department.objects.create(name='test', about='test')
        self.faculty = Faculty.objects.create(name='test', about='test', department=self.department)
        self.institute = Institute.objects.create(name='test', about='test', department=self.department)
        self.teacher = Teacher.objects.create(name='test', photo='', status='test', contact='test',
                                              department=self.department)
        self.building = Building.objects.create(name='test', location='test', floor=1)
        self.classroom = Classroom.objects.create(name='test', floor=1, about='test', building=self.building)
        self.group = Group.objects.create(name='test', department=self.department)

    def test_model_create_PreUniversity(self):
        self.new_cnt = PreUniversity.objects.count()
        self.assertNotEqual(self.old_cnt1, self.new_cnt)

    def test_model_create_Department(self):
        self.new_cnt = Department.objects.count()
        self.assertNotEqual(self.old_cnt2, self.new_cnt)

    def test_model_create_Faculty(self):
        self.new_cnt = Faculty.objects.count()
        self.assertNotEqual(self.old_cnt3, self.new_cnt)

    def test_model_create_Institute(self):
        self.new_cnt = Institute.objects.count()
        self.assertNotEqual(self.old_cnt4, self.new_cnt)

    def test_model_create_Teacher(self):
        self.new_cnt = Teacher.objects.count()
        self.assertNotEqual(self.old_cnt5, self.new_cnt)

    def test_model_create_Building(self):
        self.new_cnt = Building.objects.count()
        self.assertNotEqual(self.old_cnt6, self.new_cnt)

    def test_model_create_Classroom(self):
        self.new_cnt = Classroom.objects.count()
        self.assertNotEqual(self.old_cnt7, self.new_cnt)

    def test_model_create_Group(self):
        self.new_cnt = Group.objects.count()
        self.assertNotEqual(self.old_cnt8, self.new_cnt)

    def test_api_get_preuniversity(self):
        response = self.client.get(
            reverse('preuniversity'),
            kwargs={'pk': self.preuniversity.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.preuniversity)

    def test_api_get_department(self):
        response = self.client.get(
            reverse('department'),
            kwargs={'pk': self.department.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.department)

    # def test_api_get_faculty(self):
    #     response = self.client.get(
    #         reverse('faculty'),`
    #         kwargs={'pk': self.faculty.id}
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, self.faculty)

    # def test_api_get_institute(self):
    #     response = self.client.get(
    #         reverse('institute'),
    #         kwargs={'pk': self.institute.id}
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, self.institute)

    def test_api_get_teacher(self):
        response = self.client.get(
            reverse('teacher'),
            kwargs={'pk': self.teacher.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.teacher)

    def test_api_get_building(self):
        response = self.client.get(
            reverse('building'),
            kwargs={'pk': self.building.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.building)

    def test_api_get_classroom(self):
        response = self.client.get(
            reverse('classroom'),
            kwargs={'pk': self.classroom.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.classroom)

    def test_api_get_group(self):
        response = self.client.get(
            reverse('group'),
            kwargs={'pk': self.group.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.group)

    def test_api_get_preuniversity_detail(self):
        response = self.client.get('/preuniversity/%s/' % self.preuniversity.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            (response.data['name'], response.data['about']),
            ('test', 'test')
        )

    def test_api_get_department_detail(self):
        response = self.client.get('/department/%s/' % self.department.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            (response.data['name'], response.data['about']),
            ('test', 'test')
        )

    # def test_api_get_faculty_detail(self):
    #     response = self.client.get('/faculty/%s/' % self.faculty.id)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(
    #         (response.data['name'], response.data['about']),
    #         ('test', 'test')
    #     )

    # def test_api_get_institute_detail(self):
    #     response = self.client.get('/institute/%s/' % self.institute.id)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(
    #         (response.data['name'], response.data['about']),
    #         ('test', 'test')
    #     )
