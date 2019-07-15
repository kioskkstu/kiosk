from django.db import models


class PreUniversity(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pre-university preparation'
        verbose_name_plural = 'Pre-university preparations'


class Department(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    department = models.ForeignKey(Department, related_name="faculties", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Institute(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    department = models.ForeignKey(Department, related_name="institutes", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='teachers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Building(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()
    about = models.TextField()
    building = models.ForeignKey(Building, related_name='classrooms', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'


class Group(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, related_name='groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
