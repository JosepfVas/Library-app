from django_filters.rest_framework import DjangoFilterBackend
from books.filters import BookFilter
from books.models import Book, BookStatus
from books.serializers import BookSerializer, BookStatusSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone


# CRUD для книг

class BookCreateAPIView(generics.CreateAPIView):
    """ Создание книги """

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListAPIView(generics.ListAPIView):
    """ Список всех книг """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одной книги """

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(generics.UpdateAPIView):
    """ Обновление книги """

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDeleteAPIView(generics.DestroyAPIView):
    """ Удаление книги """

    queryset = Book.objects.all()


# ----------------------------------------------------------------

# CRUD для статуса книг

class BookStatusListAPIView(generics.ListAPIView):
    """ Список всех статусов книг """

    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all()


class BookStatusRetrieveAPIView(generics.ListAPIView):
    """ Вывод статуса одной книги """

    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all()


class TakeBookView(APIView):
    """ Взять книгу """

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if BookStatus.objects.filter(book=book, status='borrowed').exists():
            return Response({'error': 'Книга на данный момент занята'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = BookStatusSerializer(data={
            'book': book.id,
            'user': request.user.id,  # Получение текущего пользователя
            'status': 'borrowed'
        })
        if serializer.is_valid():
            serializer.save()
            book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookView(APIView):

    def post(self, request, book_id):
        book_status = get_object_or_404(BookStatus, book_id=book_id, user=request.user, status='borrowed')
        book_status.status = 'available'
        book_status.returned_at = timezone.now()
        book_status.save()
        return Response({'status': 'Книга возвращена!'}, status=status.HTTP_200_OK)
