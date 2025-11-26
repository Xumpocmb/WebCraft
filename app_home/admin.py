from django.contrib import admin

# Register your models here.
from .models import Service, Price, ContactSubmission, ContactInfo, SiteSettings

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'submitted_at', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'contact', 'message')
    date_hierarchy = 'submitted_at'

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('allow_contact_submissions', 'updated_at')
    list_editable = ('allow_contact_submissions',)
    readonly_fields = ('created_at', 'updated_at')
    list_display_links = None  # Убираем ссылки с элементов списка, так как мы редактируем первый элемент
    
    def has_add_permission(self, request):
        # Запретить добавление новых записей, так как используется синглтон
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Запретить удаление записи, так как используется синглтон
        return False

admin.site.register(Service)
admin.site.register(Price)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(ContactInfo)
admin.site.register(SiteSettings, SiteSettingsAdmin)
