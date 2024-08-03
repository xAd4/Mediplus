from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.

# Blog Page
class PostListView(ListView):
    model = Post
    template_name = "blog/blog-single.html"