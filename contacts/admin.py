from django.contrib import admin

from contacts.models import Address, Email, PhoneNumber


@admin.register(PhoneNumber)
class AdminPhoneNumber(admin.ModelAdmin):
    list_display = [
        'phone_number',
    ]


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = [
        'address',
    ]


@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    list_display = [
        'email',
    ]
