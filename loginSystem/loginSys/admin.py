from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin # To hash the password

# Register your models here.
@admin.register(MyUser)
class CustomMyUser(UserAdmin):
    pass