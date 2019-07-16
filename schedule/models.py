from django.db import models

from university.models import *

TIME_CHOICES = (
    (1, '8:00-9:20'),
    (2, '9:30-10:50'),
    (3, '11:00-12:20'),
    (4, '13:00-14:20'),
    (5, '14:30-15:50'),
    (6, '16:00-17:20'),
)

DAY_CHOICES = (
    (1, 'ПН'),
    (2, 'ВТ'),
    (3, 'СР'),
    (4, 'ЧТ'),
    (5, 'ПТ'),
    (6, 'СБ'),
)

WEEK_CHOICES = (
    (1, 'Числ'),
    (2, 'Знам'),
)

TYPE_CHOICES = (
    (1, 'Лк'),
    (2, 'Пр'),
    (3, 'Лб'),
)


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Schedule(models.Model):
    time = models.IntegerField(choices=TIME_CHOICES, default=1)
    day_of_week = models.IntegerField(choices=DAY_CHOICES, default=1)
    week = models.IntegerField(choices=WEEK_CHOICES, default=1)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name='classrooms', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='groups', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

