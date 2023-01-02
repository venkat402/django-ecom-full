from django.contrib import admin

# Register your models here.
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields()]


admin.site.register(Category, CategoryAdmin)
