from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		fields = {'name', 'start_time', 'end_time', 'memo', 'user'}
