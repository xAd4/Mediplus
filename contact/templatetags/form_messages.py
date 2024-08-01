from django import template
from contact.forms import ContactMessagesForm

register = template.Library()

@register.inclusion_tag("contact/forms/messages_form.html", takes_context=True)
def show_messages_form(context):
    request = context["request"]
    if request.user.is_authenticated:
        form = ContactMessagesForm()
        return {"form":form}
    else:
        return {"form": None}