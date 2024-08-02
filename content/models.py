from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Comments
from django.db import models
from django.contrib.auth.models import User

class PostBlog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    article = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostBlog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return f'{self.user.username}: {self.comment[:20]}'
