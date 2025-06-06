from rest_framework import serializers
from .models import ForecastModel, YieldForecast

class ForecastModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastModel
        fields = '__all__'

class YieldForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldForecast
        fields = '__all__'
