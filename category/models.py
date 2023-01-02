from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='categories/', blank=True, null=True, default='no_image/product-no-image.jpeg')
    banner = models.ImageField(upload_to='categories/', blank=True, null=True, default='no_image/banner-no-image.jpeg')
    description = models.TextField(blank=True, null=True)
    offer = models.CharField(blank=True, null=True, max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
