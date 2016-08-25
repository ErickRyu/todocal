from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Schedule
from django.utils import timezone
from .forms import ScheduleForm

# Create your views here.
def schedule_list(request):
	schedules = Schedule.objects.order_by('start_time')
	

	return render(request, 'todocal_web/schedule_list.html', {'schedules' : schedules})	

def schedule_detail(request, pk):
	schedule = get_object_or_404(Schedule, pk=pk)

	return render(request, 'todocal_web/schedule_detail.html', {'schedule': schedule})



def schedule_new(request):
	if request.method == "POST":
		form = ScheduleForm(request.POST)
		if form.is_valid():
			schedule = form.save(commit=False)
			schedule.save()
			return redirect('schedule_detail', pk=schedule.pk)
	else:
		form = ScheduleForm()
	return render(request, 'todocal_web/schedule_edit.html', {'form' : form})