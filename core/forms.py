from django import forms
from .models import DepartmentAppointment

class DepartmentAppointmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentAppointment
        fields = ["name_patient", "email_patient", "phone_patient", "department", "content"]
        widgets = {
            "name_patient": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name of patient", "style":"text-transform:none;",}),
            "email_patient": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email of patient", "style":"text-transform:none;",}),
            "phone_patient": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone of patient", "style":"text-transform:none;",}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Reason for appointment", "style":"text-transform:none;",}),
        }
