from django.db import models

# Create your models here.

# Department List
class DepartmentList(models.Model):
    department = models.CharField(max_length=20, verbose_name="Department")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.department


# Appointment
class DepartmentAppointment(models.Model):
    name_patient = models.CharField(max_length=50, verbose_name="Name of patient")
    email_patient = models.EmailField(max_length=50, verbose_name="Email of patient")
    phone_patient = models.CharField(max_length=15, verbose_name="Phone of patient")
    department = models.ForeignKey(DepartmentList, on_delete=models.CASCADE, null=False, verbose_name="Department List")
    content = models.CharField(max_length=600, verbose_name="Reason for appointment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return self.name_patient




