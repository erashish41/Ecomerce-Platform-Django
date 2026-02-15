from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ("email", "username", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    
    ordering = ("-date_joined",)
    search_fields = ("email", "username")
    
    readonly_fields = ("last_login", "date_joined")
