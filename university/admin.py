from django.contrib import admin
from .models import *


class DepartmentInlines(admin.StackedInline):
    model = Department
    extra = 1


class GroupInlines(admin.StackedInline):
    model = Group
    extra = 1


class TeacherInlines(admin.StackedInline):
    model = Teacher
    extra = 1


class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentInlines, ]


class InstituteAdmin(admin.ModelAdmin):
    inlines = [DepartmentInlines, ]


class ClassroomInlines(admin.StackedInline):
    model = Classroom
    extra = 1


class BuildingAdmin(admin.ModelAdmin):
    inlines = [ClassroomInlines, ]


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [TeacherInlines, GroupInlines]


admin.site.register(PreUniversity,)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher, )
admin.site.register(Building, BuildingAdmin)
admin.site.register(Classroom, )
admin.site.register(Group, )
