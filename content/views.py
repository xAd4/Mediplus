from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BlogTemplateView(TemplateView):
    template_name = "content/blog-single.html"