from django.db import models

class ForecastModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class YieldForecast(models.Model):
    plot = models.ForeignKey('crops.Plot', on_delete=models.CASCADE)
    forecast_model = models.ForeignKey(ForecastModel, on_delete=models.SET_NULL, null=True)
    forecast_date = models.DateField()
    predicted_yield = models.FloatField()
    notes = models.TextField(blank=True, null=True)
