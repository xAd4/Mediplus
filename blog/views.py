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
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Obtén el objeto del post de manera segura

        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_published = request.user
            comment.save()
            return redirect('blog-detail', pk=post.pk)  # Redirige para evitar resubmisiones

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


# Comments

# Comment Detail
class CommentDetailView(DetailView):
    pass