from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('time', 'day_of_week', 'week', 'teacher', 'subject', 'group', 'classroom', )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
