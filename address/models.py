from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model


# Create your models here.
class Address(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    type = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
