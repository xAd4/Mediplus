from django import template
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.forms import DepartmentAppointmentForm

register = template.Library()

@register.inclusion_tag("core/forms/appointment_form.html", takes_context=True)
def show_page_form(context):
    request = context['request']
    if request.user.is_authenticated:
        form = DepartmentAppointmentForm()
        return {"form": form}
    else:
        return {"form": None}
