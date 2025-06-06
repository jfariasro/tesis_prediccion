from rest_framework import routers
from .views import CropViewSet, PlotViewSet, CropEventViewSet

router = routers.DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'plots', PlotViewSet)
router.register(r'events', CropEventViewSet)

urlpatterns = router.urls
