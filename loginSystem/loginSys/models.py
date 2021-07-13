from django.db import models
from django.contrib.auth.models import AbstractUser


# Extended user table
class MyUser(AbstractUser):
    age = models.IntegerField(verbose_name="Insert your age", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

class Title(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()