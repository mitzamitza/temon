from rest_framework import serializers

from monitor.models import Values


class TempSerializer(serializers.ModelSerializer):

    class Meta:
        model = Values
        fields = ('sensor', 'temperature')