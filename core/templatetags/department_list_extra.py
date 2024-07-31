from django import template
from core.models import DepartmentList

register = template.Library()

@register.simple_tag
def get_department_list():
    list = DepartmentList.objects.all()
    return list