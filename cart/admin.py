from django.contrib import admin

# Register your models here.
from cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]


admin.site.register(Cart, CartAdmin)
