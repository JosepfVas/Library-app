from django.contrib import admin
from authors.models import Author


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fullname",
    )
    list_filter = ("fullname",)
    search_fields = ("fullname",)
