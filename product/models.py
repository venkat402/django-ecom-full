from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photos = models.ImageField(upload_to='products/', blank=True, null=True, default='no_image/product-no-image.jpeg')
    price = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    offer = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
