from rest_framework import serializers
from .models import Crop, Plot, CropEvent

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'

class CropEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropEvent
        fields = '__all__'
