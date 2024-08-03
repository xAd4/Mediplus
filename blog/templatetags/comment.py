from django import template
from blog.models import Comment

register = template.Library()

@register.simple_tag
def get_comment_list():
    comments = Comment.objects.all()
    return comments