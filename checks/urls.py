from rest_framework.routers import DefaultRouter
from .views import CheckViewSet

router = DefaultRouter()
router.register(r'checks', CheckViewSet)

urlpatterns = router.urls