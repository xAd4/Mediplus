from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Blog Page
class BlogTemplateView(TemplateView):
    template_name = "blog/blog-single.html"