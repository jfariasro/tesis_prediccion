from django.db import models

class SensorData(models.Model):
    plot = models.ForeignKey('crops.Plot', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    sensor_type = models.CharField(max_length=100)
    value = models.FloatField()

class WeatherData(models.Model):
    plot = models.ForeignKey('crops.Plot', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()

class HistoricalYield(models.Model):
    plot = models.ForeignKey('crops.Plot', on_delete=models.CASCADE)
    year = models.IntegerField()
    yield_amount = models.FloatField()
