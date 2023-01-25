from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    list_display_links = ["username", "email", "first_name"]
    readonly_fields = ["last_login", "date_joined"]

    def change_view(self, request, object_id, form_url="", extra_context=None):
        self.exclude = ["password"]
        return super().change_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url="", extra_context=None):
        self.exclude = None
        return super().add_view(request, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.set_password(obj.password)
        obj.save()
