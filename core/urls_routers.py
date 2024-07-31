from rest_framework import routers
from .api import DepartmentAppointmentViewSet, DepartmentListViewSet

# Router Appointments

router = routers.DefaultRouter()
router.register("api/appointments", DepartmentAppointmentViewSet, basename="api-appointment")
router.register("api/list", DepartmentListViewSet, basename="api-list")
urlpatterns = router.urls
