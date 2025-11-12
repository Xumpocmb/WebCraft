from django.contrib import admin

# Register your models here.
from .models import Service, Price, ContactSubmission

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'submitted_at', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'contact', 'message')
    date_hierarchy = 'submitted_at'

admin.site.register(Service)
admin.site.register(Price)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
