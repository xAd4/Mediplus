from rest_framework import viewsets
from .models import DepartmentAppointment, DepartmentList
from .serializers import DepartmentAppointmentSerializer, DepartmentListSerializer

# ViewSet Appointment API
class DepartmentAppointmentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentAppointment.objects.all()
    serializer_class = DepartmentAppointmentSerializer

# ViewSet List API
class DepartmentListViewSet(viewsets.ModelViewSet):
    queryset = DepartmentList.objects.all()
    serializer_class = DepartmentListSerializer