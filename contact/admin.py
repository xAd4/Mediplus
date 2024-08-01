from django.contrib import admin
from .models import ContactMessages


# Register your models here.

class ContactMessagesAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    
admin.site.register(ContactMessages, ContactMessagesAdmin)
