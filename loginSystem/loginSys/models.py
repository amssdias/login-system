from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Extended user table
class MyUser(AbstractUser):
    age = models.IntegerField(verbose_name="Insert your age", blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)