from django.contrib import admin
from .models import *


class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1
    fields = ('name', 'about')


class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]


class InstituteAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline, ]


admin.site.register(PreUniversity)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Building)
admin.site.register(Classroom)
admin.site.register(Group)
