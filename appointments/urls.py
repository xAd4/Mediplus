from django.urls import path
from . import views

urlpatterns = [
    path("", views.MedicalAppointmentsListView.as_view(), name="medical-appointments"),
    path("<int:pk>/", views.MedicalAppointmentsDetailView.as_view(), name="medical-appointments-detail"),
    path("delete/<int:pk>/", views.MedicalAppointmentDeleteView.as_view(), name="medical-appointments-delete"),
]
