from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import DepartmentAppointmentForm
from django.shortcuts import redirect

# Create your views here.

# Home Page
class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DepartmentAppointmentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DepartmentAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-200-ok')  # Redirige a la misma página después de guardar
        return self.get(request, *args, **kwargs, form=form)

# Portfolio and Projects Page
class PortfolioTemplateView(TemplateView):
    template_name = "core/portfolio-details.html"

# Blog Page
class BlogTemplateView(TemplateView):
    template_name = "core/blog-single.html"

# Contact Page
class ContactTemplateView(TemplateView):
    template_name = "core/contact.html"

class PostOKTemplateView(TemplateView):
    template_name = "core/post_200_ok.html"