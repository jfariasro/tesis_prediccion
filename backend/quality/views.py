from rest_framework import viewsets
from .models import QualityInspection, QualityParameter, QualityResult
from .serializers import QualityInspectionSerializer, QualityParameterSerializer, QualityResultSerializer

class QualityInspectionViewSet(viewsets.ModelViewSet):
    queryset = QualityInspection.objects.all()
    serializer_class = QualityInspectionSerializer

class QualityParameterViewSet(viewsets.ModelViewSet):
    queryset = QualityParameter.objects.all()
    serializer_class = QualityParameterSerializer

class QualityResultViewSet(viewsets.ModelViewSet):
    queryset = QualityResult.objects.all()
    serializer_class = QualityResultSerializer
