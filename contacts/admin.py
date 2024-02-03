from django.contrib import admin

from contacts.models import Contact


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'type',
        'data',
    ]
