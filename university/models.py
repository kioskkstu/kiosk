from django.db import models

from schedule.models import ScheduleOfTeacher, ScheduleOfGroup


class PreUniversity(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()


class Institute(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()


class Department(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    faculty = models.ForeignKey(Faculty, related_name='departments',
                                on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, related_name='departments_institute',
                                  on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='teachers',
                                   on_delete=models.CASCADE)
    schedule_of_teacher = models.ForeignKey(ScheduleOfTeacher, related_name='teachers_for_schedule',
                                            on_delete=models.CASCADE)
    schedule_of_group = models.ForeignKey(ScheduleOfGroup, related_name='teacher_for_group',
                                          on_delete=models.CASCADE)


class Building(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()
    about = models.TextField()
    building = models.ForeignKey(Building, related_name='classrooms', on_delete=models.CASCADE)
    schedule_of_teacher = models.ForeignKey(ScheduleOfTeacher, related_name='classroom_for_schedule',
                                            on_delete=models.CASCADE)
    schedule_of_group = models.ForeignKey(ScheduleOfGroup, related_name='classroom_for_group',
                                          on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, related_name='groups', on_delete=models.CASCADE)
    schedule_of_teacher = models.ForeignKey(ScheduleOfTeacher, related_name='schedule_of_teacher',
                                            on_delete=models.CASCADE)
    schedule_of_group = models.ForeignKey(ScheduleOfGroup, related_name='schedule_of_group',
                                          on_delete=models.CASCADE)