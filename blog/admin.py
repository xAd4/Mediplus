from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    
admin.site.register(Post, PostAdmin)

# Comment Register

class PostComment(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    
admin.site.register(Comment, PostComment)
