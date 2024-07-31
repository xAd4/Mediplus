from django import template
from core.models import DepartmentAppointment

register = template.Library()

@register.simple_tag
def get_appointment_list():
    appointments = DepartmentAppointment.objects.all()
    return appointments