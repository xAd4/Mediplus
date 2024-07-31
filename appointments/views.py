from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from core.models import DepartmentAppointment
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

# Create your views here.

# SEGURITY METHOD
class StaffIsRequired(object): # Método de seguridad
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequired, self).dispatch(request, *args, **kwargs)

class MedicalAppointmentsListView(ListView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments.html"

class MedicalAppointmentsDetailView(DetailView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments_detail.html"   

# Delete Medical Appointment

@method_decorator(staff_member_required, name="dispatch")
class MedicalAppointmentDeleteView(DeleteView):
    model = DepartmentAppointment
    template_name = "forms/default_form_delete.html"
    success_url = reverse_lazy("medical-appointments")
