# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20170314_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='values',
            options={'get_latest_by': 'time'},
        ),
    ]
