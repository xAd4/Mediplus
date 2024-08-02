from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Comments
class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comment User")
    post = models.ForeignKey("PostBlog", on_delete=models.CASCADE, verbose_name="Relation Post")
    comment = models.CharField(max_length=500, verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return self.user.username
    
# Posts
class PostBlog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title post")
    content = models.TextField(verbose_name="Content post")
    article = models.CharField(max_length=400, verbose_name="Article post")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title