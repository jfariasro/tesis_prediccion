from rest_framework import viewsets
from .models import SensorData, WeatherData, HistoricalYield
from .serializers import SensorDataSerializer, WeatherDataSerializer, HistoricalYieldSerializer

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class HistoricalYieldViewSet(viewsets.ModelViewSet):
    queryset = HistoricalYield.objects.all()
    serializer_class = HistoricalYieldSerializer
