from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^monitor/$',  views.temp_list, name='temp_list'),
    url(r'^monitor/(?P<sensor_id>[0-9]+)$', views.temp_detail, name='temp_detail'),
]