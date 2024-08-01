from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BlogCommentForm

# Create your views here.

class BlogTemplateView(TemplateView):
    template_name = "blog/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        form = BlogCommentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('post-200-ok')
        return self.get(request, *args, **kwargs, form=form)