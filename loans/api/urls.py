from loans.api.views import LoanViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LoanViewSet, base_name='Loan')
urlpatterns = router.urls
