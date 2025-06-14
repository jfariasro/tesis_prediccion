# Generated by Django 5.0.6 on 2025-06-06 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalYield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('yield_amount', models.FloatField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.plot')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sensor_type', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.plot')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.plot')),
            ],
        ),
    ]
