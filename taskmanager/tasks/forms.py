from django import forms
from .models import Timesheet

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = [
            'task',
            'week_start',
            'monday_hours',
            'tuesday_hours',
            'wednesday_hours',
            'thursday_hours',
            'friday_hours',
            'notes',
        ]
