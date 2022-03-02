from rest_framework.routers import SimpleRouter

from applications.product.views import ProductViewSet

router = SimpleRouter()
router.register('', ProductViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
