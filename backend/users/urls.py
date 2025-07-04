from rest_framework import routers
from .views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = router.urls
