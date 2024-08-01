from django.urls import path
from . import views

urlpatterns = [
    path("", views.MedicalAppointmentsListView.as_view(), name="medical-appointments"),
    path("<int:pk>/", views.MedicalAppointmentsDetailView.as_view(), name="medical-appointments-detail"),
    path("delete/<int:pk>/", views.MedicalAppointmentDeleteView.as_view(), name="medical-appointments-delete"),
    # CONTACT
    path("contact/messages", views.ContactMessagesListView.as_view(), name="messages"),
    path("contact/messages/<int:pk>/", views.ContactMessagesDetailView.as_view(), name="messages-detail"),
    path("contact/messages/delete/<int:pk>/", views.ContactMessagesDeleteView.as_view(), name="messages-delete"),
]
