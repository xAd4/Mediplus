from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Comments
class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return self.user.username