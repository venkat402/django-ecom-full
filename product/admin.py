from django.contrib import admin

# Register your models here.
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]


admin.site.register(Product, ProductAdmin)
