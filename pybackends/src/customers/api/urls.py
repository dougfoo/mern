from customers.api.views import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CustomerViewSet, basename='customer')
urlpatterns = router.urls
