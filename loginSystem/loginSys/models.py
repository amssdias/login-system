from django.db import models
from django.contrib.auth.models import AbstractUser


# Extended user table
class MyUser(AbstractUser):
    age = models.IntegerField(verbose_name="Insert your age", blank=True, null=True)