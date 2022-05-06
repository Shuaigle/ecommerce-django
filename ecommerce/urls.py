from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ecommerce.drf.views import AllProductsViewsets

router = routers.DefaultRouter()
router.register(
    r'home', AllProductsViewsets, basename="allproducts"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include(("ecommerce.demo.urls", "demo"), namespace="demo")),
    path("", include(router.urls)),
]
