from django import forms
from .models import ContactMessages

class ContactMessagesForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name of patient", "style":"text-transform:none;",}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email of patient", "style":"text-transform:none;",}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone of patient", "style":"text-transform:none;",}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject of message", "style":"text-transform:none;",}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Reason for message", "style":"text-transform:none;",}),
        }