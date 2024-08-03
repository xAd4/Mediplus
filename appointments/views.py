from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from core.models import DepartmentAppointment
from contact.models import ContactMessages
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

# Create your views here.

# SEGURITY METHOD
class StaffIsRequired(object): # Método de seguridad
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequired, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name="dispatch")
class MedicalAppointmentsListView(ListView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments.html"

@method_decorator(staff_member_required, name="dispatch")
class MedicalAppointmentsDetailView(DetailView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments_detail.html"   

# Delete Medical Appointment

@method_decorator(staff_member_required, name="dispatch")
class MedicalAppointmentDeleteView(DeleteView):
    model = DepartmentAppointment
    template_name = "forms/default_form_delete.html"
    success_url = reverse_lazy("medical-appointments")

# MESSAGES

@method_decorator(staff_member_required, name="dispatch")
class ContactMessagesListView(ListView):
    model = ContactMessages
    template_name = "appointments/messages.html"

@method_decorator(staff_member_required, name="dispatch")
class ContactMessagesDetailView(DetailView):
    model = ContactMessages
    template_name = "appointments/messages_detail.html"   

# Delete Medical Appointment

@method_decorator(staff_member_required, name="dispatch")
class ContactMessagesDeleteView(DeleteView):
    model = ContactMessages
    template_name = "forms/default_form_delete.html"
    success_url = reverse_lazy("messages")
