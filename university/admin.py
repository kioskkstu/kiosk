from django.contrib import admin
from .models import *


class PreUniversityAdmin(admin.ModelAdmin):
    fields = ['name', 'about']


class FacultyAdmin(admin.ModelAdmin):
    fields = ['name', 'about']


class InstituteAdmin(admin.ModelAdmin):
    fields = ['name', 'about']


class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'about', 'faculty', 'institute']


class TeacherAdmin(admin.ModelAdmin):
    fields = ['name', 'photo', 'status', 'contact', 'department', 'schedule_of_teacher', 'schedule_of_group']


class BuildingAdmin(admin.ModelAdmin):
    fields = ['name', 'location', 'floor']


class ClassroomAdmin(admin.ModelAdmin):
    fields = ['name', 'floor', 'about', 'schedule_of_teacher', 'schedule_of_group']


class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'department', 'schedule_of_teacher', 'schedule_of_group']


admin.site.register(PreUniversity, PreUniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Group, GroupAdmin)
