from django.contrib import admin
from .models import QualityInspection, QualityParameter, QualityResult

admin.site.register(QualityInspection)
admin.site.register(QualityParameter)
admin.site.register(QualityResult)
