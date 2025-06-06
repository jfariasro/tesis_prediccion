from django.contrib import admin
from .models import Crop, Plot, CropEvent

admin.site.register(Crop)
admin.site.register(Plot)
admin.site.register(CropEvent)
