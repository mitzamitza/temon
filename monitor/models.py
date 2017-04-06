from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    sensor_ip = models.GenericIPAddressField(protocol='IPv4')
    sensor_model = models.CharField(max_length=90)
    picture = models.CharField(max_length=1000)
    current_temperature = models.FloatField(max_length=100)

    def get_absolute_url(self):
        return reverse('monitor:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.name + ' - ' + self.sensor_model + ' --------- ' + str(self.current_temperature) + ' grade'

class Values(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.temperature) + ' ' +  str(self.time)

    class Meta:
        get_latest_by = 'time'

class Thermostat(models.Model):
    temperature = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.temperature)
