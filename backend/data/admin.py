from django.contrib import admin
from .models import SensorData, WeatherData, HistoricalYield

admin.site.register(SensorData)
admin.site.register(WeatherData)
admin.site.register(HistoricalYield)
