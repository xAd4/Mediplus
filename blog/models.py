from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Post
class Post(models.Model):
    user_published = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    article = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return f"{self.user_published.username} - {self.title[20:]}"