from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# 200 OK Template View. When sent one message or one appointment, show this template
class PostOKTemplateView(TemplateView):
    template_name = "helpers/post_200_ok.html"