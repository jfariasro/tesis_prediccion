from rest_framework import routers
from .views import QualityInspectionViewSet, QualityParameterViewSet, QualityResultViewSet

router = routers.DefaultRouter()
router.register(r'quality-inspections', QualityInspectionViewSet)
router.register(r'quality-parameters', QualityParameterViewSet)
router.register(r'quality-results', QualityResultViewSet)

urlpatterns = router.urls
