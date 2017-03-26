from django.http import Http404
from django.shortcuts import render, render_to_response
from .models import Sensor, Values
from chartit import DataPool, Chart
from django.db.models import Q
from monitor.models import Values
from datetime import datetime, timedelta
from .fusioncharts import FusionCharts

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

def sensors(request):
    all_sensors = Sensor.objects.all()
    return render(request, 'monitor/sensors.html', {'all_sensors' : all_sensors})


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
               'source': Values.objects.filter(time__gte=time_24_hours_ago).filter(Q(time__minute=00)).filter(sensor_id__exact=3)},

              'terms': [
                'time',
                'temperature']},
             ],

        )

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'spline',
                  'lineWidth' : 3,

                  'stacking': True},
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


def chart(request):
    time_24_hours_ago = datetime.now() - timedelta(days=1)
    dataSource = {}
    dataSource1 = {}
    dataSource2 = {}

    #seriesname = []
    dataSource['chart'] = [{
        "caption": "Temperatures",
        "subCaption": "24 hours temperaturess",
        "captionPadding": "15",
        "showvalues": "1",
        "valueFontColor": "#ffffff",
        "placevaluesInside": "1",
        "usePlotGradientColor": "0",
        "legendShadow": "1",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateVGridColor": "0",
        "alignCaptionWithCanvas": "0",
        "legendPadding": "15",
        "plotToolText": "<div><b>$label</b><br/>Temperatura : <b>$value grade</b></div>",
        "theme": "fint"
    }]

    dataSource['categories'] = [{
        "category": [{
            "label": "Z1"
        }, {
            "label": "Z2"
        },{
            "label": "Z3"
        }, {
            "label": "Z4"
        }, {
            "label": "Z5"
        },{
            "label": "Z6"
        }, {
            "label": "Z7"
        },{
            "label": "Z8"
        }, {
            "label": "Z9"
        }, {
            "label": "Z10"
        },{
            "label": "Z11"
        }, {
            "label": "Z12"
        }]
    }]


    dataSource1['data'] = []
    dataSource2['data'] = []
    dataSource['dataset'] = []

    for key in Values.objects.filter(time__gte=time_24_hours_ago).filter(Q(time__minute=00)).filter(sensor_id__exact=1):
        data = {}
        data['label'] = str(key.time)
        data['value'] = key.temperature
        dataSource1['data'].append(data)

    for key2 in Values.objects.filter(time__gte=time_24_hours_ago).filter(Q(time__minute=00)).filter(sensor_id__exact=3):
        data2 = {}
        data2['label'] = str(key2.time)
        data2['value'] = key2.temperature
        dataSource2['data'].append(data2)

    d1 = { "data" : dataSource1['data']}
    d2 = { "data" : dataSource2['data']}
    dataSource['dataset'].append(d1)
    dataSource['dataset'].append(d2)
    #dataSource['dataset'] =  [{ "data" : dataSource1['data'] , "data": dataSource2['data']}]




        #dataSource['data'] + dataSource['data2']



    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("msspline", "ex1", "900", "400", "chart-1", "json", dataSource)
#    return render_to_response('monitor/bhart.html', {'output' : column2d.render()})
    return render(request, 'monitor/bhart.html', {'output' : column2d.render()})



