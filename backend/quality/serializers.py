from rest_framework import serializers
from .models import QualityInspection, QualityParameter, QualityResult

class QualityInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspection
        fields = '__all__'

class QualityParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityParameter
        fields = '__all__'

class QualityResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityResult
        fields = '__all__'
