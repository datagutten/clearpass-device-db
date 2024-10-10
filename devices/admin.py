from django.contrib import admin

from devices import models


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role', 'description']


# Register your models here.
@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['mac', 'expiry', 'enabled']
    list_filter = ['enabled']
