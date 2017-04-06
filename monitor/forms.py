from django import forms
from monitor.models import Thermostat

class Tedit(forms.ModelForm):

    class Meta:
        model = Thermostat
        fields = ('temperature',)