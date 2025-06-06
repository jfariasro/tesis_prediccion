from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Plot(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    area = models.FloatField()

class CropEvent(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
