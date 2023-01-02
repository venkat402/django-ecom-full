from django.contrib import admin

# Register your models here.
from subscribe.models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscribe._meta.get_fields()]


admin.site.register(Subscribe, SubscribeAdmin)
