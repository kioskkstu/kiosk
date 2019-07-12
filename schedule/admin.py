from django.contrib import admin

from .models import *


class SubjectAdmin(admin.ModelAdmin):
    fields = ['name', 'schedule_of_teacher', 'schedule_of_group']
    admin.site.register(Subject, SubjectAdmin)


class ScheduleOfTeacher(admin.ModelAdmin):
    fields = ['time', 'day_of_week', 'week', 'date']
    admin.site.register(ScheduleOfTeacher, ScheduleOfTeacherAdmin)


class ScheduleOfGroup(admin.ModelAdmin):
    fields = ['time', 'day_of_week', 'week', 'date']
    admin.site.register(ScheduleOfGroup, ScheduleOfGroupAdmin)