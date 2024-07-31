from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import DepartmentAppointment

# Create your views here.

class MedicalAppointmentsListView(ListView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments.html"

class MedicalAppointmentsDetailView(DetailView):
    model = DepartmentAppointment
    template_name = "appointments/medical_appointments_detail.html"   
