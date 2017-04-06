from django.conf.urls import url

from . import views


urlpatterns = [
    # /monitor/
    url(r'^$', views.index, name='index'),

    # /monitor/sensor
    url(r'^(?P<sensor_id>[0-9]+)/$', views.detail, name='detail'),

    # chart
    url(r'^chart/$', views.chart, name='chart'),

    # bhart
    url(r'^bhart/$', views.chart, name='bhart'),

    # Sensors
    url(r'^sensors/$', views.sensors, name='sensors'),

    # thermostat
    url(r'^thermostat/$', views.thermostat, name='thermostat'),

    # Sensor Add
    url(r'^sensors/add/$', views.sensoradd, name='sensors-add'),

]