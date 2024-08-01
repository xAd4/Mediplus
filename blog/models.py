from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# OPTIMIZATION
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = BlogPost.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'post/' + filename

# Create your models here.

# Blog
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    user_published = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user_post")
    content = models.TextField()
    article = models.CharField(max_length=500, blank=True, null=True)
    comments = models.ManyToManyField(User, related_name="blog_post_comments")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
 
    class Meta:
        verbose_name = "Post"
        verbose_name = "Posts"
        
    def __str__(self):
        return f"{self.title} - {self.user_published}"  


# Comments
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
    
    
# OPTIMIZATION MEDIA
@receiver(post_delete, sender=BlogPost)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)