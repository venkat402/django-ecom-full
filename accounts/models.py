from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS
    objects = CustomUserManager()
