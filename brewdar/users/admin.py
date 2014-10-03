from django.contrib import admin
from models import User, Device


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_id', 'name', 'verification_token',
                    'verified', 'authentication_token', 'authenticated', 'user']

admin.site.register(User, UserAdmin)
admin.site.register(Device, DeviceAdmin)
