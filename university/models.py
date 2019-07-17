from django.db import models


class PreUniversity(models.Model):
    name = models.CharField(max_length=40, verbose_name='Name')
    about = models.TextField(verbose_name='About')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pre-university preparation'
        verbose_name_plural = 'Pre-university preparations'


class Faculty(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    about = models.TextField(verbose_name='About')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Institute(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    about = models.TextField(verbose_name='About')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    about = models.TextField(verbose_name='About')
    faculty = models.ForeignKey(Faculty, related_name="departments_of_faculty", verbose_name='Faculty',
                                on_delete=models.CASCADE, null=True, blank=True)
    institute = models.ForeignKey(Institute, related_name="departments_of_institute", verbose_name='Institute',
                                  on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    photo = models.ImageField(null=True, blank=True, verbose_name='Photo')
    status = models.CharField(max_length=50, verbose_name='Status')
    contact = models.CharField(max_length=50, verbose_name='Contact')
    department = models.ForeignKey(Department, related_name='teachers',
                                   on_delete=models.CASCADE, verbose_name='Department')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Building(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    floor = models.PositiveIntegerField(verbose_name='Floor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'


class Classroom(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    floor = models.PositiveIntegerField(verbose_name='Floor')
    about = models.CharField(null=True, max_length=50, verbose_name='About')
    building = models.ForeignKey(Building, related_name='classrooms',
                                 on_delete=models.CASCADE, verbose_name='Building')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'


class Group(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    department = models.ForeignKey(Department, related_name='groups',
                                   on_delete=models.CASCADE, verbose_name='Department')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
