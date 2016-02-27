from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import PointsViewSet

router.register(r'points', PointsViewSet)
urlpatterns = router.urls
