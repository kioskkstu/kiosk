from django.db import models


class PreUniversity(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()


class Department(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    department = models.ForeignKey(Department, related_name="faculties", on_delete=models.CASCADE)


class Institute(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='teachers',
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


class Group(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, related_name='groups', on_delete=models.CASCADE)
