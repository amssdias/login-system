from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin  # To hash the password


@admin.register(MyUser)
class CustomMyUser(UserAdmin):
    list_display = ('username', 'age')
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Information", {
            'fields': ('age',)
        }),
    )
