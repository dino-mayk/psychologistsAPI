from django.contrib import admin

from books.models import Book


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = [
        'title',
    ]
