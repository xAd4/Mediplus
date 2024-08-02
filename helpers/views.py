from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# 200 OK
class PostOKTemplateView(TemplateView):
    template_name = "helpers/post_200_ok.html"