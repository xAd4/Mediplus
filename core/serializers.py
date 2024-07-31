from rest_framework import serializers
from .models import DepartmentAppointment, DepartmentList
# Serializer Appointments
class DepartmentAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentAppointment
        fields = ["name_patient", "email_patient", "phone_patient", "department", "content"]


# Serializer List

class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentList
        fields = ["department"]


