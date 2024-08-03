from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

# Blog Page
class PostListView(ListView):
    model = Post
    template_name = "blog/blog-single.html"
  
# Blog Page Detail  
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog-single-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=self.kwargs['pk'])
            comment.user_published = request.user  # Usa el nombre del campo correcto
            comment.save()
            return redirect('blog-detail', pk=self.kwargs['pk'])  # Asegúrate de que esta URL sea la correcta
        return self.get(request, *args, **kwargs, form=form)

    
# Comments

# Comment Detail
class CommentDetailView(DetailView):
    pass