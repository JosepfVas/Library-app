from rest_framework import generics
from authors.models import Author
from authors.paginators import AuthorsPaginator
from authors.serializers import AuthorSerializer
from books.permissions import IsModer, IsLibrarian, IsReader
from rest_framework.permissions import IsAuthenticated

# CRUD для автора.


class AuthorCreateAPIView(generics.CreateAPIView):
    """Создание автора"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian]


class AuthorListAPIView(generics.ListAPIView):
    """Список всех авторов"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = AuthorsPaginator


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одного автора"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian | IsReader]


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """Обновление автора"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsLibrarian]


class AuthorDeleteAPIView(generics.DestroyAPIView):
    """Удаление автора"""

    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
