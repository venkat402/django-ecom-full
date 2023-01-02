from django.contrib import admin

# Register your models here.
from cart.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]


class CartItemsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.fields]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemsAdmin)
