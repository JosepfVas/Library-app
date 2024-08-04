import django_filters
from books.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.CharFilter(
        field_name="author__fullname", lookup_expr="icontains"
    )
    written_year = django_filters.CharFilter(lookup_expr="icontains")
    genre = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["title", "author", "written_year", "genre"]
