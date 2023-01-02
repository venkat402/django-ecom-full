from django.contrib import admin

# Register your models here.
from product.models import Product, Review, Favorite


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]


class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]


class FavoriteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Favorite._meta.fields]


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)
