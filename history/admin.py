from django.contrib import admin
from .models import *


class HistoryAdmin(admin.ModelAdmin):
    fields = ['name', 'text']


admin.site.register(History, HistoryAdmin)
