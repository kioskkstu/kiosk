from django.contrib import admin
from .models import *


class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1
    fields = ('name', 'name_ru', 'name_en', 'name_kg', 'about', 'about_ru', 'about_en', 'about_kg')
    ordering = ['name', ]


class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]
    ordering = ['name', ]


class InstituteAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]
    ordering = ['name', ]


class ClassroomInline(admin.StackedInline):
    model = Classroom
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class ClassroomAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class BuildingAdmin(admin.ModelAdmin):
    inlines = [ClassroomInline, ]


class GroupAdmin(admin.ModelAdmin):
    ordering = ['name', 'department', 'grade', ]
    list_display = ['name', 'department', 'grade', ]


admin.site.register(PreUniversity)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Classroom, ClassroomAdmin)
