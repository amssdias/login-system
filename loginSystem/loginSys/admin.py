from django.contrib import admin
from .models import MyUser, Title
from django.contrib.auth.admin import UserAdmin  # To hash the password


@admin.register(MyUser)
class CustomMyUser(UserAdmin):
    list_display = ('username', 'age')
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Information", {
            'fields': ('age',)
        }),
    )


@admin.register(Title)
class CustomMyUser(admin.ModelAdmin):
    # fields = [field.name for field in Title._meta.get_fields()]
    fieldsets = (
        ("Create your first title", {
            'fields': ('title', 'description')
        }),
    )
