from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from address.models import Address


# Create your models here.
class Cart(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    address_id = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="address_ids"
    )
    shipping_id = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="shipping"
    )
    discount = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
