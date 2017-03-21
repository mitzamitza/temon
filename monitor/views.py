from django.http import Http404
from django.shortcuts import render, render_to_response
from .models import Sensor, Values
from chartit import DataPool, Chart
from django.db.models import Q
from monitor.models import Values
from datetime import datetime, timedelta

#from .decorators import add_source_code_and_doc


def index(request):
    all_sensors = Sensor.objects.all()
#   all_values = []

#    def sf():
#    for sensoir in all_sensors:
#        caca = Values.objects.filter(id__exact=sensoir.id).order_by('-id')[0]
#        all_values.append(caca.temperature)


    all_values = Values.objects.all()


    return render(request, 'monitor/index.html', {'all_sensors' : all_sensors, 'all_values' : all_values})

def detail(request, sensor_id):
    try:
        sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        raise Http404("INEXISTENT")
    return render(request, 'monitor/detail.html', {'sensor' : sensor})


"""
The chart part starts here
"""
def weather_chart_view(request):
    time_24_hours_ago = datetime.now() - timedelta(days=1)
    time_10_minutes_ago = datetime.now() - timedelta(minutes=10)
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': Values.objects.filter(time__gte=time_24_hours_ago).filter(Q(time__minute=00) | Q(time__minute=30) )},
               #'source': Values.objects.filter(time__date=time_24_hours_ago).filter(Q(time__minute=30) | Q(time__minute=00) )},
              'terms': [
                'time',
                'temperature']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'time': [
                    'temperature']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Graficele de temperatura'},
               'xAxis': {
                    'title': {
                       'text': 'Ora'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('monitor/chart.html', {'wchart' : cht})


