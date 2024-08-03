from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


# Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'post/' + filename

# Create your models here.

# Post
class Post(models.Model):
    user_published = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    article = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return f"{self.user_published.username} - {self.title[20:]}"
    
# Method Security 1.2
@receiver(post_delete, sender=Post)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)