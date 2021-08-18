from loginSys.validators import validate_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validators import validate_password, validate_domain_email


# Extended user table
class MyUser(AbstractUser):
    age = models.IntegerField(verbose_name="Insert your age", blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, unique=True, validators=[validate_domain_email])
    password = models.CharField(_('password'), max_length=128)

    def capitalize_names(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    def save(self, *args, **kwargs):
        self.capitalize_names()
        super(MyUser, self).save(*args, **kwargs)