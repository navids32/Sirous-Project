from django.contrib import admin

from .models import *


admin.site.register(UserProfile)


class ModelItemAdmin(admin.ModelAdmin):
    list_display = ['model_item']


admin.site.register(ModelItem, ModelItemAdmin)


class BrandItemAdmin(admin.ModelAdmin):
    list_display = ['brand_item']


admin.site.register(BrandItem, BrandItemAdmin)


class StatusItemAdmin(admin.ModelAdmin):
    list_display = ['status_item']


admin.site.register(StatusItem, StatusItemAdmin)


class AnyItemAdmin(admin.ModelAdmin):
    search_fields = ['serial_number']
    list_display = ['serial_number', 'model_item', 'brand_item', 'status_item', 'location', 'date_in']


admin.site.register(AnyItem, AnyItemAdmin)