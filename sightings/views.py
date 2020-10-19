from django.shortcuts import render, get_object_or_404, redirect
from .models import Squirrel
from django.http import HttpResponse
from .forms import SquirrelForm, SquirrelForm_
from django.db.models import Max,Count,Avg,Min

# Create your views here.
'''
def index(request):
    return HttpResponse('Hello!')
'''

def list(request):
    squirrels = Squirrel.objects.order_by('unique_squirrel_id')
    context = {'squirrels': squirrels} 
    return render(request, 'sightings/sightings.html', context)

def update(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form':form,
    }
    return render(request, 'sightings/update.html', context)

def stats(request):	
	scd = Squirrel.objects
#   scd2 = Squirrel
	data_count = scd.count()
	Unique_Squirrel_ID_count = scd.count()
	Date_min = scd.filter().aggregate(Min('date'))["date__min"]
	Date_max = scd.filter().aggregate(Max('date'))["date__max"]
	Age_Adult_count = scd.filter(age = "ADULT").count()
	Age_Juvenile_count = scd.filter(age = "JUVENILE").count()
	Shift_AM_count = scd.filter(shift = "AM").count()
	Shift_PM_count = scd.filter(shift = "PM").count()
	Latitude_min = scd.filter().aggregate(Min('latitude'))["latitude__min"]
	Latitude_max = scd.filter().aggregate(Max('latitude'))["latitude__max"]
	Latitude_avg = scd.filter().aggregate(Avg('latitude'))["latitude__avg"]
	Longitude_min = scd.filter().aggregate(Min('longitude'))["longitude__min"]
	Longitude_max = scd.filter().aggregate(Max('longitude'))["longitude__max"]
	Longitude_avg = scd.filter().aggregate(Avg('longitude'))["longitude__avg"]

	dic = {
		"data_count": data_count,
		"Unique_Squirrel_ID_count": Unique_Squirrel_ID_count,
		"Date_min": Date_min,
		"Date_max": Date_max,
		"Age_Adult_count": Age_Adult_count,
		"Age_Juvenile_count": Age_Juvenile_count,
		"Shift_AM_count": Shift_AM_count,
		"Shift_PM_count": Shift_PM_count,
		"Latitude_min": Latitude_min,
		"Latitude_max": Latitude_max,
		"Latitude_avg": Latitude_avg,
		"Longitude_min": Longitude_min,
		"Longitude_max": Longitude_max,
		"Longitude_avg": Longitude_avg,
	}
	return render(request, 'sightings/stats.html',dic)