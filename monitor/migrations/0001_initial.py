# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('sensor_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('sensor_model', models.CharField(max_length=90)),
                ('picture', models.CharField(max_length=1000)),
                ('current_temperature', models.FloatField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Sensor')),
            ],
        ),
    ]
