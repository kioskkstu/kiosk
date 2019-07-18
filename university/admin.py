from django.contrib import admin
from .models import *


class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1
    fields = ('name', 'about', 'name_en', 'about_en', 'name_kg', 'about_kg')


class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]


class InstituteAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]


class ClassroomInline(admin.StackedInline):
    model = Classroom
    extra = 1


class BuildingAdmin(admin.ModelAdmin):
    inlines = [ClassroomInline, ]


admin.site.register(PreUniversity)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Group)
