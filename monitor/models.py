from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    sensor_ip = models.GenericIPAddressField(protocol='IPv4')
    sensor_model = models.CharField(max_length=90)
    picture = models.CharField(max_length=1000)
    current_temperature = models.FloatField(max_length=100)
    def __str__(self):
        return self.name + ' - ' + self.sensor_model

class Values(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.temperature) + ' ' +  str(self.time)