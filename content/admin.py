from django.contrib import admin
from .models import BlogComment, PostBlog


# Register your models here.

class BlogCommentAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(PostBlog)

