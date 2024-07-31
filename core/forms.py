from django import forms
from .models import DepartmentAppointment

class DepartmentAppointmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentAppointment
        fields = ["name_patient", "email_patient", "phone_patient", "department", "content"]
        widgets = {
            "name_patient": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name of patient",}),
            "email_patient": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email of patient"}),
            "phone_patient": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone of patient"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Reason for appointment"}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.label = ''
