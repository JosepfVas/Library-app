from django_filters.rest_framework import DjangoFilterBackend
from books.filters import BookFilter
from books.models import Book, BookStatus
from books.paginators import BooksPaginator
from books.permissions import IsReader, IsModer, IsLibrarian
from books.serializers import BookSerializer, BookStatusSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger("books")


# CRUD для книг


class BookCreateAPIView(generics.CreateAPIView):
    """Создание книги"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian]


class BookListAPIView(generics.ListAPIView):
    """Список всех книг"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BooksPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    permission_classes = [IsAuthenticated, IsReader | IsModer | IsLibrarian]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одной книги"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsReader | IsModer | IsLibrarian]


class BookUpdateAPIView(generics.UpdateAPIView):
    """Обновление книги"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated | IsModer | IsLibrarian]


class BookDeleteAPIView(generics.DestroyAPIView):
    """Удаление книги"""

    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


# ----------------------------------------------------------------

# CRUD для статуса книг


class BookStatusListAPIView(generics.ListAPIView):
    """Список всех статусов книг"""

    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all().order_by("id")
    pagination_class = BooksPaginator
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian]


class BookStatusRetrieveAPIView(generics.ListAPIView):
    """Вывод статуса одной книги"""

    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian]


class TakeBookView(APIView):
    """Взять книгу"""

    permission_classes = [IsAuthenticated, IsReader]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if BookStatus.objects.filter(book=book, status="borrowed").exists():
            return Response(
                {"error": "Книга на данный момент занята"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        book_status = BookStatus.objects.create(
            book=book,
            user=request.user,
            status="borrowed",
            taken_at=timezone.now(),
            returned_at=None,
        )

        logger.info(
            f"Пользователь {request.user.username} взял книгу {book.title} в {book_status.taken_at}"
        )

        return Response({"status": "Книга взята!"}, status=status.HTTP_201_CREATED)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated, IsReader]

    def post(self, request, book_id):
        book_status = get_object_or_404(BookStatus, book_id=book_id, status="borrowed")

        book_status.status = "available"
        book_status.returned_at = timezone.now()
        book_status.save()

        logger.info(
            f"Книга возвращена пользователем :{request.user.fullname} в {timezone.now()}"
        )

        return Response(
            {
                "status": f"Книга возвращена пользователем :{request.user.fullname} в {timezone.now()}"
            },
            status=status.HTTP_200_OK,
        )
