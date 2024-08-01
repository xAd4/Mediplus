from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import DepartmentAppointmentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

# Home Page
class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DepartmentAppointmentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        form = DepartmentAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('post-200-ok')
        return self.get(request, *args, **kwargs, form=form)


# Portfolio and Projects Page
class PortfolioTemplateView(TemplateView):
    template_name = "core/portfolio-details.html"

class PostOKTemplateView(TemplateView):
    template_name = "core/post_200_ok.html"