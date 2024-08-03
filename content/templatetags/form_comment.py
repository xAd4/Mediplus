from django import template
from content.forms import BlogCommentForm

register = template.Library()

@register.inclusion_tag("content/forms/form_comment.html", takes_context=True)
def show_comment_form(context):
    request = context["request"]
    if request.user.is_authenticated:
        form = BlogCommentForm()
        return {"form":form}
    else:
        return {"form":None}