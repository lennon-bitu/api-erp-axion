from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, SupplierViewSet, EmployeeViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = router.urls