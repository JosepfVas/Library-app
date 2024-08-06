from rest_framework.serializers import ModelSerializer
from books.models import Book, BookStatus


class BookSerializer(ModelSerializer):
    """Сериализатор книг"""

    class Meta:
        model = Book
        fields = "__all__"


class BookStatusSerializer(ModelSerializer):
    """Сериализатор статуса книг"""

    class Meta:
        model = BookStatus
        fields = "__all__"
