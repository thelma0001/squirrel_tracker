from django.shortcuts import render
from sightings.models import Squirrel

# Create your views here.

def map(request):
    # to show the first 100 sightings of the list
    sightings = Squirrel.objects.all()[0:100]
    context = {
        'sightings': sightings,
    }

    return render(request, 'map/map.html', context)
