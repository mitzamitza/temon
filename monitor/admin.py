from django.contrib import admin
from .models import Sensor, Values

admin.site.register(Sensor)
admin.site.register(Values)