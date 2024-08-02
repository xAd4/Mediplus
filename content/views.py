from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .forms import BlogCommentForm
from .models import PostBlog

# Create your views here.
class BlogTemplateView(ListView):
    template_name = "content/blog-single.html"
    model = PostBlog
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            post_id = request.POST.get('post_id')
            if post_id:
                comment.post_id = post_id  # Asigna el post_id del formulario
                comment.save()
                return redirect('post-200-ok')
            else:
                form.add_error(None, "No se ha proporcionado un ID de post válido.")
        return self.get(request, *args, **kwargs, form=form)