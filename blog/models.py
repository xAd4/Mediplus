from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    comment = models.CharField(max_length=600, verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Comment"
        verbose_name = "Comments"
        
    def __str__(self):
        return self.user