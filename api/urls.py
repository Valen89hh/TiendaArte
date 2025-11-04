from rest_framework import routers
from .views import GaleriaViewSet, ObraViewSet

router = routers.DefaultRouter()
router.register(r'galerias', GaleriaViewSet)
router.register(r'obras', ObraViewSet)

urlpatterns = router.urls
