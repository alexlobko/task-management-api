from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "full_name",
        "position",
        "deputy",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("full_name", "position", "deputy")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("full_name", "position", "deputy",)}),)


admin.site.register(CustomUser, CustomUserAdmin)