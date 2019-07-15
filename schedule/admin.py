from django.contrib import admin

from .models import *
from university.admin import TeacherInlines, ClassroomInlines, GroupInlines


class SubjectInLines(admin.StackedInline):
    model = Subject
    extra = 1


class ScheduleOfTeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherInlines, SubjectInLines, GroupInlines, ClassroomInlines, ]


class ScheduleOfGroupAdmin(admin.ModelAdmin):
    inlines = [TeacherInlines, SubjectInLines, GroupInlines, ClassroomInlines, ]


admin.site.register(Subject)
admin.site.register(ScheduleOfTeacher, ScheduleOfTeacherAdmin)
admin.site.register(ScheduleOfGroup, ScheduleOfGroupAdmin)

