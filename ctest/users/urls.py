from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import UserViewSet

router.register(r'users', UserViewSet)
urlpatterns = router.urls
