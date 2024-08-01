from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ContactMessages
from .forms import ContactMessagesForm

# Create your views here.

class ContactTemplateView(TemplateView):
    template_name = "contact/contact.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactMessagesForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        form = ContactMessagesForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('post-200-ok')
        return self.get(request, *args, **kwargs, form=form)

