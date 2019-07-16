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
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
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
    name = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    time = models.IntegerField(choices=TIME_CHOICES, default=1, verbose_name='Time')
    day_of_week = models.IntegerField(choices=DAY_CHOICES, default=1, verbose_name='Day of the week')
    week = models.IntegerField(choices=WEEK_CHOICES, default=1, verbose_name='Week')
    type_of_lecture = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name='Type of lecture')
    teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE, verbose_name='Teacher')
    classroom = models.ForeignKey(Classroom, related_name='classrooms',
                                  on_delete=models.CASCADE, verbose_name='Classroom')
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE, verbose_name='Subject')
    group = models.ForeignKey(Group, related_name='groups', on_delete=models.CASCADE, verbose_name='Group')

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
