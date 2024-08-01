from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactMessages(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name of user")
    email = models.EmailField(max_length=100, verbose_name="Email of user")
    phone = models.CharField(max_length=15, verbose_name="Phone of user")
    subject = models.CharField(max_length=50, verbose_name="Subject of user")
    message = models.CharField(max_length=600, verbose_name="Message of user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User of database")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return f"{self.name} - {self.subject}"
