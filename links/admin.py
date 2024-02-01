from django.contrib import admin

from links.models import Link


@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    list_display = [
        'domain',
    ]
