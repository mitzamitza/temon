from django.http import Http404
from django.shortcuts import render, render_to_response, redirect
from django.db.models import Q
from .models import Sensor, Values, Thermostat
from .forms import Tedit
from chartit import DataPool, Chart
from monitor.models import Values
from monitor.models import Thermostat
from datetime import datetime, timedelta
from .fusioncharts import FusionCharts
from  django.views.generic import CreateView, UpdateView, DeleteView

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
        "xaxisname": "Ora",
        "yaxisname": "Temperatura",
        "showvalues": "0",
        "showLegend" : "1",
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
        "drawCrossLine": "0",
        "palettecolors": "#f8bd19,#e44a00,#33bdda,#008ee4,#6baa01,#583e78",
        "plotToolText": "<div>Ora:<b>$label:00</b><br/>Temperatura : <b>$value grade</b></div>",
        "theme": "fint"
    }]
    lst = []
    for k in range(1, 25):
        caca = (datetime.now() + timedelta(hours=k))
        ch = float(caca.hour)
        lst.append({'label': ch})

    dataSource['categories'] = [{
        "category": lst
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
    d3 = {"seriesname": "Birou"}
    d4 = {"seriesname": "Exterior"}

    dataSource['dataset'].append(d3)
    dataSource['dataset'].append(d1)
    dataSource['dataset'].append(d4)
    dataSource['dataset'].append(d2)


    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("msspline", "ex1", "700", "300", "chart-1", "json", dataSource)
#    return render_to_response('monitor/bhart.html', {'output' : column2d.render()})
    return render(request, 'monitor/chart.html', {'output' : column2d.render()})

def thermostat(request):
    if request.method == 'POST':
        form = Tedit(request.POST)

        if form.is_valid():
            post = form.save(commit=True)
            post.save
            return redirect('thermostat')
        else:
            print(form.errors)

    else:
        form = Tedit()
    return render(request, 'monitor/thermostat.html', {'form' : form})

def sensoradd(CreateView):
    model = Sensor
    fields = ['name', 'location', 'sensor_ip', 'sensor_model', 'picture']






