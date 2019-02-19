from customers.api.views import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CustomerViewSet, base_name='customer')
urlpatterns = router.urls
