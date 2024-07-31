from django import template
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
