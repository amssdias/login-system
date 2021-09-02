from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # To hash the password

from .models import MyUser


@admin.register(MyUser)
class CustomMyUser(UserAdmin):
    list_display = ('id', 'username', 'age')
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Information", {
            'fields': ('age',)
        }),
    )
    ordering = ('-date_joined',)

