from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Service, ContactRequest, Comment, SiteSettings


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ("author", "created_at")


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ("name", "price", "active")
    list_filter = ("active",)
    search_fields = ("name",)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "phone_number", "message")
    list_editable = ("status",)
    readonly_fields = ("phone_number", "message", "created_at")
    inlines = [CommentInline]
    fieldsets = (
        (None, {"fields": ("name", "phone_number", "message", "created_at")}),
        ("Management", {"fields": ("status",)}),
    )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Comment) and not instance.pk:
                instance.author = request.user
            instance.save()
        formset.save_m2m()


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("accept_requests", "updated_at")
    fieldsets = (("Настройки формы заявок", {"fields": ("accept_requests",), "description": "Включите или отключите прием заявок с формы на сайте"}),)

    def has_add_permission(self, request):
        # Only allow one instance of SiteSettings
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the SiteSettings instance
        return False
