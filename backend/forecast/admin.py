from django.contrib import admin
from .models import ForecastModel, YieldForecast

admin.site.register(ForecastModel)
admin.site.register(YieldForecast)
