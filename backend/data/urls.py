from rest_framework import routers
from .views import SensorDataViewSet, WeatherDataViewSet, HistoricalYieldViewSet

router = routers.DefaultRouter()
router.register(r'sensor-data', SensorDataViewSet)
router.register(r'weather-data', WeatherDataViewSet)
router.register(r'historical-yield', HistoricalYieldViewSet)

urlpatterns = router.urls
