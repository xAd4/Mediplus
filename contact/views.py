from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ContactTemplateView(TemplateView):
    template_name = "contact/contact.html"
