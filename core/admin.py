from django.contrib import admin
from .models import DepartmentList, DepartmentAppointment

# Register your models here.

# Register Department List and Config
class DepartmentListAdmin(admin.ModelAdmin):
    search_fields = ("department",)
    readonly_fields = ("created_at", "updated_at")

admin.site.register(DepartmentList, DepartmentListAdmin)

# Register DepartmentAppointment and Config

class DepartmentAppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("department",)
    search_fields = ("name_patient",)
    ordering = ("created_at",)

admin.site.register(DepartmentAppointment, DepartmentAppointmentAdmin)







