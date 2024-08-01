from django import template
from blog.forms import BlogCommentForm

register = template.Library()

@register.inclusion_tag("blog/forms/comment_form.html", takes_context=True)
def show_comment_form(context):
    request = context['request']
    if request.user.is_authenticated:
        form = BlogCommentForm()
        return {"form": form}
    else:
        return {"form": None}