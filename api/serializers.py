from rest_framework import serializers

from monitor.models import Values, Sensor


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = ('sensor', 'temperature', 'time')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'location', 'sensor_ip')

