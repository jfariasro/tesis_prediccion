from rest_framework import routers
from .views import ForecastModelViewSet, YieldForecastViewSet

router = routers.DefaultRouter()
router.register(r'forecast-models', ForecastModelViewSet)
router.register(r'yield-forecasts', YieldForecastViewSet)

urlpatterns = router.urls
