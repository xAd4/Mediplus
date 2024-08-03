from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


# SECURITY METHOD
"""class StaffIsRequired(object): 
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffIsRequired, self).dispatch(request, *args, **kwargs)"""

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
    
    
# Blog CRUD - Only Staff's
@method_decorator(staff_member_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = "forms/default_form_create.html"
    fields = ["title", "content", "image", "article"]
    success_url = reverse_lazy("blog")
    
    def form_valid(self, form):
        form.instance.user_published = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class = None): 
        form = super(PostCreateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2",})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2",})
        form.fields["article"].widget = forms.Textarea(attrs={"class": "form-control mb-2",})
        form.fields["image"].widget = forms.ClearableFileInput()
        return form
    
@method_decorator(staff_member_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    template_name = "forms/default_form_update.html"
    fields = ["title", "content", "image", "article"]
    success_url = reverse_lazy("blog")
    
    def get_form(self, form_class = None): 
        form = super(PostUpdateView, self).get_form()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2",})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2",})
        form.fields["article"].widget = forms.Textarea(attrs={"class": "form-control mb-2",})
        form.fields["image"].widget = forms.ClearableFileInput()
        return form
    

@method_decorator(staff_member_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post
    template_name = "forms/default_form_delete.html"
    success_url = reverse_lazy("blog")

# Comments
# Comment Delete
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "forms/default_form_delete.html"
    context_object_name = "object"
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user_published or self.request.user.is_superuser
    
    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('blog-detail', kwargs={'pk': comment.post.id})