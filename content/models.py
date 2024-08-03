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
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comment User")
    post = models.ForeignKey("PostBlog", on_delete=models.CASCADE, verbose_name="Relation Post")
    comment = models.CharField(max_length=500, verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostBlog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> 2714c173b9b943c70a5cc942bd498e1f9a698bd0
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
    def __str__(self):
<<<<<<< HEAD
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
=======
        return f'{self.user.username}: {self.comment[:20]}'
>>>>>>> 2714c173b9b943c70a5cc942bd498e1f9a698bd0
