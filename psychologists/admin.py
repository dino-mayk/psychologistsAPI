from django.contrib import admin

from psychologists.models import Psychologist


@admin.register(Psychologist)
class AdminPsychologist(admin.ModelAdmin):
    list_display = [
        'name',
        "surname",
        "patronymic",
    ]
