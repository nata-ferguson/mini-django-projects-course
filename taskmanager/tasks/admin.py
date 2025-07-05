from django.contrib import admin
from .models import Task, Timesheet

admin.site.register(Task)

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('project', 'week_start', 'user', 'status')

admin.site.register(Timesheet, TimesheetAdmin)
