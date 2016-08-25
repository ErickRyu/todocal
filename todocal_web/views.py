from django.shortcuts import render
from .models import User, Schedule
from django.utils import timezone

# Create your views here.
def schedule_list(request):
	schedules = Schedule.objects.order_by('start_time')
	

	return render(request, 'todocal_web/schedule_list.html', {'schedules' : schedules})	
