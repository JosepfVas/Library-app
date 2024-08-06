from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "written_year",
        "genre",
    )
    list_filter = ("author",)
    search_fields = ("author", "title", "genre")
