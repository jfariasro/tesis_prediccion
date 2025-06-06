from rest_framework import serializers
from .models import SensorData, WeatherData, HistoricalYield

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class HistoricalYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalYield
        fields = '__all__'
