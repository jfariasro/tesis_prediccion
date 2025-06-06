from rest_framework import viewsets
from .models import Crop, Plot, CropEvent
from .serializers import CropSerializer, PlotSerializer, CropEventSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

class CropEventViewSet(viewsets.ModelViewSet):
    queryset = CropEvent.objects.all()
    serializer_class = CropEventSerializer
