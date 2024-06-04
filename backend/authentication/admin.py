from authentication.models import UserModified
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(UserModified)
class UserModifiedAdmin(UserAdmin):
    list_display = (
        "email", "is_admin", "is_staff", "is_superuser", "date_join"
    )
    search_fields = ("email",)
    list_filter = ("is_admin", "is_superuser", "is_staff")
    readonly_fields = ("is_superuser", "is_active")
    search_help_text = "available search by email"

    ordering = ('email',)

    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()