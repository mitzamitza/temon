from django.http import Http404
from django.shortcuts import render
from .models import Sensor

def index(request):
    all_sensors = Sensor.objects.all()
    return render(request, 'monitor/index.html', {'all_sensors' : all_sensors})

def detail(request, sensor_id):
    try:
        sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        raise Http404("INEXISTENT")
    return render(request, 'monitor/detail.html', {'sensor' : sensor})