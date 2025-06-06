from rest_framework import viewsets
from .models import ForecastModel, YieldForecast
from .serializers import ForecastModelSerializer, YieldForecastSerializer

class ForecastModelViewSet(viewsets.ModelViewSet):
    queryset = ForecastModel.objects.all()
    serializer_class = ForecastModelSerializer

class YieldForecastViewSet(viewsets.ModelViewSet):
    queryset = YieldForecast.objects.all()
    serializer_class = YieldForecastSerializer
