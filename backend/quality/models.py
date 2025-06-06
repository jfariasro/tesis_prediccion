from django.db import models

class QualityParameter(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)

class QualityInspection(models.Model):
    plot = models.ForeignKey('crops.Plot', on_delete=models.CASCADE)
    date = models.DateField()
    inspector = models.CharField(max_length=100)

class QualityResult(models.Model):
    inspection = models.ForeignKey(QualityInspection, on_delete=models.CASCADE)
    parameter = models.ForeignKey(QualityParameter, on_delete=models.CASCADE)
    value = models.FloatField()
