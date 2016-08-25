from django.shortcuts import render, get_object_or_404
from .models import User, Schedule
from django.utils import timezone

# Create your views here.
def schedule_list(request):
	schedules = Schedule.objects.order_by('start_time')
	

	return render(request, 'todocal_web/schedule_list.html', {'schedules' : schedules})	

def schedule_detail(request, pk):
	schedule = get_object_or_404(Schedule, pk=pk)

	return render(request, 'todocal_web/schedule_detail.html', {'schedule': schedule})