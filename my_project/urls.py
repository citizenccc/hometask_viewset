from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from applications.product.urls import router
from applications.product.views import ProductViewSet
from my_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
