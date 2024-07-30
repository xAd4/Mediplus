from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Home Page
class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

# Portfolio and Projects Page
class PortfolioTemplateView(TemplateView):
    template_name = "core/portfolio-details.html"

# Blog Page
class BlogTemplateView(TemplateView):
    template_name = "core/blog-single.html"

# Contact Page
class ContactTemplateView(TemplateView):
    template_name = "core/contact.html"

# Error 404 Page
class ErrorTemplateView(TemplateView):
    template_name = "core/404.html"