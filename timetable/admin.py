from django.contrib import admin

from timetable.models import Timetable


@admin.register(Timetable)
class AdminPsychologist(admin.ModelAdmin):
    list_display = [
        'presenter',
        "theme",
    ]
