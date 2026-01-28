from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductVariationViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'product-variations', ProductVariationViewSet, basename='productvariation')

urlpatterns = router.urls
